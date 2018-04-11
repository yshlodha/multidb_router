from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from django.template import Context, Template

PRODUCT_CATEGORY = (('sports', 'sports'),
                    ('electronics', 'electronics'),
                    ('fashion', 'fashion'))

db_list = list([db for db in settings.DATABASES.keys()])


class Database(models.Model):
    """
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DatabaseUser(models.Model):
    """
    """
    user = models.OneToOneField(User)
    databases = models.ManyToManyField(Database)
    notification = models.BooleanField(default=True)


class Product(models.Model):
    """
    """
    user = models.ForeignKey(DatabaseUser)
    name = models.CharField(max_length=255)
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=255,
                                null=True, default=None)


@receiver(post_save, sender=DatabaseUser)
def my_callback(sender, instance, created, **kwargs):
    if created and instance.notification:
        import inspect
        records = []
        for frame_record in inspect.stack():
            records.append(frame_record[3])
            from_email = settings.DEFAULT_EMAIL_ADDRESS
            if (frame_record[3] == 'get_response'):
                request = frame_record[0].f_locals['request']
                email = request.POST.get('email')
                username = request.POST.get('username')
                password1 = request.POST.get('password1')
                domain = settings.DOMAIN
                message = "Hi, your login credentials are given"\
                           " below:\n\tusername: {{ username }}\n\t"\
                           "password: {{password}}\n\nplease go to {{ domain}}{% url 'login' %} and"\
                           " login"
                template = Template(message)
                context = Context({'username': username, 'password': password1, 'domain': domain})
                email_body = template.render(context)
                send_mail('Login Credential Email', email_body, from_email, [email])

@receiver(m2m_changed, sender=DatabaseUser.databases.through)
def multidb_user_creation(sender, instance, action, **kwargs):
    if action=='post_add' and instance.notification:
        dbs = instance.databases.all()
        for db in dbs:
            user = User(username=instance.user.username, password=instance.user.password, email=instance.user.email)
            user.id = instance.user.id
            user.save(using=db.name)
            dbuser = DatabaseUser(user=user, notification=False)
            dbuser.id = instance.id
            dbuser.save(using=db.name, force_insert=True)



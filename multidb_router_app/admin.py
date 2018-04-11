from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from multidb_router_app.models import DatabaseUser, Product

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class DatabaseUserInline(admin.StackedInline):
    model = DatabaseUser
    can_delete = False
    verbose_name_plural = 'db_user'


class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True


class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {'fields': ('username', 'email',
                                        'password1', 'password2'), 'classes': ('wide',)}),)
    inlines = (DatabaseUserInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


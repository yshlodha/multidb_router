from .models import *


def get_product_list(user):
    """
    :param user:
    :return:
    """
    product_list = []
    try:
        dbuser = DatabaseUser.objects.get(user__username=user.username)
        dbs = dbuser.databases.all()
        for db in dbs:
            products = Product.objects.using(db.name).filter(user__id=dbuser.id)
            if products:
                product_list.append({db.name: products})
    except DatabaseUser.DoesNotExist:
        return []
    return product_list

def get_user_dbs(user):
    """
    :param user:
    :return:
    """
    try:
        dbuser = DatabaseUser.objects.get(user__username=user.username)
        db_list = [db.name for db in dbuser.databases.all()]
    except DatabaseUser.DoesNotExist:
        return []
    return db_list

def get_dbuser(username):
    """
    :param username:
    :return:
    """
    try:
        dbuser = DatabaseUser.objects.get(user__username=username)
    except DatabaseUser.DoesNotExist:
        return None
    return dbuser

def add_product_to_db(user, name, category, database):
    """
    :param user:
    :param name:
    :param category:
    :param database:
    :return:
    """
    try:
        dbuser = DatabaseUser.objects.get(user__username=user.username)
        product_object = Product(user_id=dbuser.id, category=category, name=name)
        product_object.save(using=database)
    except DatabaseUser.DoesNotExist:
        return False
    return True


def get_all_user_products():
    """
    :return:
    """
    users = []
    dbusers = DatabaseUser.objects.filter(user__is_superuser=False)
    for dbuser in dbusers:
        products = get_product_list(dbuser.user)
        if products:
            users.append({dbuser.user.username: products})
    return users

def delete_product(username, product_id, db):
    """
    :param username:
    :param product_id:
    :param db:
    :return:
    """
    try:
        dbuser = DatabaseUser.objects.get(user__username=username)
    except DatabaseUser.DoesNotExist:
        return False

    try:
        product = Product.objects.using(db).get(id=product_id, user__id=dbuser.id)
    except Product.DoesNotExist:
        return False
    product.delete()
    return True
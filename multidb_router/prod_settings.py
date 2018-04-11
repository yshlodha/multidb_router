"""
Django settings for multidb_router project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*#6j1mhcuvu8(!s0iml9!*vefukt0gpi=i!6ai!3_cciw+9#w-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multidb_router_app.apps.MultidbRouterAppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'multidb_router.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'multidb_router.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'user_db',
                'USER': '',
                'PASSWORD': '',
                'HOST': ''},
    'db_1': {'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'database1',
             'USER': '',
             'PASSWORD': '',
             'HOST': ''},

    'db_2': {'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'database2',
             'USER': '',
             'PASSWORD': '',
             'HOST': ''},

    'db_3': {'ENGINE': 'django.db.backends.mysql',
             'OPTIONS': {
                         'sql_mode': 'traditional',
             },
            'NAME': 'database3',
            'USER': 'root',
            'PASSWORD': 'yash',
            'HOST': '',
            'PORT': ''},

    'db_4': {'ENGINE': 'django.db.backends.mysql',
             'OPTIONS': {
                         'sql_mode': 'traditional',
             },
             'NAME': 'database4',
             'USER': '',
             'PASSWORD': '',
             'HOST': '',
             'PORT': ''},

    'db_5': {'ENGINE': 'django.db.backends.mysql',
             'OPTIONS': {
                         'sql_mode': 'traditional',
             },
             'NAME': 'database5',
             'USER': '',
             'PASSWORD': '',
             'HOST': '',
             'PORT': ''},
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#AUTH_USER_MODEL = "multidb_router_app.DatabaseUser"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DEFAULT_EMAIL_ADDRESS = ''

DOMAIN = ''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

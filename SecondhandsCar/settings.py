"""
Django settings for SecondhandsCar project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTH_USER_MODEL = "userinfo.UserInfo"
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(1,os.path.join(BASE_DIR,'extra_apps'))
MEDIA_URL='/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')#这个是在浏览器上访问该上传文件的url的前缀
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c!a5@(1ny^m=*et%#)%lw7u)_4y_xuqq*iec1^5u3v(%357x2l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

#celery
import djcelery
djcelery.setup_loader()

BROKER_URL = 'redis://192.168.2.183:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.2.183:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.userinfo',
    'apps.buy',
    'apps.sale',
    'apps.front',
    'apps.pay',
    'apps.ORMdemo',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'rest_framework',
    'testrabbitmq',

]
from md import MyMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'md.MyMiddleware',
    'md.MyMiddleware2',

]

ROOT_URLCONF = 'SecondhandsCar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS':True,
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

WSGI_APPLICATION = 'SecondhandsCar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'secondhandscar',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':3306
    },
    'db2': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'stock',
            'USER':'root',
            'PASSWORD':'root',
            'HOST':'localhost',
            'PORT':3306
        }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR,'static')
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers':{
        'django.db.backends':{
            'handlers':['console'],
            'propagate':True,
            'level':'DEBUG',
        },
    },
}
#create database secondhandscar default charset utf8;

#邮箱配置
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
#To use port 465, you need to call smtplib.SMTP_SSL()
# if you want use PORT 465,your EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend',and
# you need to install django_smtp_ssl EMAIL_PORT=465
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465#587#25
EMAIL_HOST_USER = '1140514109@qq.com'
EMAIL_HOST_PASSWORD = 'zsmfrjnvxapkjeif'#'zsmfrjnvxapkjeif'
EMAIL_SUBJECT_PREFIX = u'django'#为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True                  #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#爬虫头部配置
HEADERS = [
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
]

#自定义COOKIES 签名采用方法的路径配置
SIGNING_BACKEND = 'utils.signcookie.MySigner'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.DjangoModelPermissionOrAnonReadOnly'
    ],
}
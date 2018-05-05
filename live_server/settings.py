# -*- coding: utf-8 -*-
"""
Django settings for live_server project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lre$m#y_@kkk71wtl1y!1i@*r8oxfot_2opw7wn&-hqv=)@sw@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lite',
    'cover',
    'room',
    'order',
    'pvp',
    'ppt',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'lite.middleware.session.SessionMiddleware',
)

ROOT_URLCONF = 'live_server.urls'


#django suit
# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'索骏TV直播平台',
    'HEADER_DATE_FORMAT': 'l, j. F Y', # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',       # 18:42

     # forms
    'SHOW_REQUIRED_ASTERISK': True, #Automatically adds asterisk symbol * to the end of every required field label:
    'CONFIRM_UNSAVED_CHANGES': True, #Alert will be shown, when you’ll try to leave page, without saving changed form first:

     # menu
    'SEARCH_URL': '/huaxun/admin/api/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
     'MENU_EXCLUDE': ('auth.group', 'auth'),#  menu不显示的栏目图标
    'MENU': (
        # sites是默认原先的app和models
        # 'sites',
        '-',
        {'app': 'lite', 'label': u'小程序', 'icon': 'icon-user',
            'models': (
                'lite.App',
                'lite.User',
                'lite.Company',
                'lite.FileLibrary',
                'lite.FileTag',
                # {'model': 'lite.FileTag', 'label': 'Staff',},
            )
        },
        {'app': 'room', 'label': u'直播间', 'icon': 'icon-leaf',
            'models': (
                'room.Room',
                'room.Message',

            )
        },
        {'app': 'cover', 'label': u'专栏', 'icon': 'icon-edit',
            'models': (
                'cover.Tag',
                'cover.News',
                'cover.Article',

            )
        },
        {'app': 'order', 'label': u'会员支付', 'icon': 'icon-tags',
            'models': (
                'order.Cost',
                'order.Member',
                'order.Order',
                # 'order.Discount',
                # 'order.DiscountTemplate',
            )
        },
        {'app': 'pvp', 'label': u'1v1课堂', 'icon': 'icon-fire',
            'models': (
                'pvp.Stage',
                'pvp.StageTag',
                'pvp.StageFile',
                'pvp.PVPMember',
            )
        },
        {'app': 'ppt', 'label': u'PPT课堂', 'icon': 'icon-fire',
            'models': (
                'ppt.PPTFile',
                'ppt.PPTTag',
                'ppt.PPTTeam',
                'ppt.PPTTeamUser',
            )
        },
        {'app': 'ppt', 'label': u'通讯录', 'icon': 'icon-fire',
            'models': (
                'ppt.PPTRosterTag',
                'ppt.PPTRoster',
            )
        },
    ),
    # misc
    'LIST_PER_PAGE': 15 #每页数量
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'live_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'live',
    #     'USER': 'root',
    #     'PASSWORD':'root',
    #     'HOST':'127.0.0.1',
    #     'PORT':'3306',
    # }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False #计算机所在地时间#


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/live/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# AUTH_USER_MODEL = "lite.AdminUser"


# log配置
# LOG_FILE = "./all.log"
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#             }
#         },
#     'formatters': {
#         'simple': {
#             'format': '[%(levelname)s] %(module)s : %(message)s'
#             },
#         'verbose': {
#             'format':
#                 '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
#             }
#         },
#
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'django.utils.log.NullHandler',
#             },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#             },
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'formatter': 'verbose',
#             'filename': LOG_FILE,
#             'mode': 'a',
#             },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false']
#             }
#         },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#          'django.request': {
#             'handlers': ['mail_admins', 'console'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }

# username:  live
# password: live
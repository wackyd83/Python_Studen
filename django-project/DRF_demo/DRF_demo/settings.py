"""
Django settings for DRF_demo project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6f8_$!gy+lo85tg5lps3_7cp)4nu0k9#tj-1_nibb0kwgn6vad'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
    'rest_framework',  # DRF框架作为插件需要注册到项目中
    'django_filters',  # Django的过滤功能模块
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DRF_demo.urls'

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

WSGI_APPLICATION = 'DRF_demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': 'www.wackyd.top',  # 数据库主机
        'PORT': 9985,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'Aa123456.',  # 数据库用户密码
        'NAME': 'books'  # 数据库名字
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DFR框架的配置信息，这里的配置信息对整个项目生效
REST_FRAMEWORK = {
    # # 认证的全局配置
    # 'DEFAULT_AUTHENTICATION_CLASSES':(
    #     'rest_framework.authentication.BasicAuthentication',  # 基本认证
    #     'rest_framework.authentication.SessionAuthentication'  # session认证
    # ),
    # # 权限的全局配置
    # 'DEFAULT_PERMISSION_CLASSES':(
    #     'rest_framework.permissions.IsAuthenticated',
    # )
    # # 全局用户限流
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.AnonRateThrottle',  # 匿名用户
    #     'rest_framework.throttling.UserRateThrottle'  # 认证用户
    # ),
    # # 指定用户限流次数
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '3/day',
    #     'user': '4/day'
    # },
    # 视图类限流
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    # 指定视图限流次数
    'DEFAULT_THROTTLE_RATES': {
        'uploads': '10/day',  # 表示uploads名称的视图每天只能访问2次
        'user': '20/day',  # 如同时进行用户和视图限流则，最下方的配置生效
    },

    # 全局过滤方法
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),

    # 全局分页器（项目中较少使用，一般都使用局部分页器）
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,  # 每页数目

    # 全局异常处理
    'EXCEPTION_HANDLER': 'book_drf.utils.exception_handler',

    # 指定接口文档大纲
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

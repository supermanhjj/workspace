"""
Django settings for digital_retina project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!b=n95@%%(yh6!20wb0ej1x9&l&%&049rs-ec=2!j2yo3vz2&%'

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
    # django add
    # digital_retina_system backend app
    'digital_retina_system.apps.DigitalRetinaSystemConfig',
    # django add
    # vue add
    # 防止跨域, django cors headers, pip install django-cors-headers
    'corsheaders',
    # 方便写后端接口, django rest framework, pip install djangorestframework
    'rest_framework',
    # vue add
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # vue add
    # 这个的导入不能太靠后，因为中间件也有先后顺序的加载
    'corsheaders.middleware.CorsMiddleware',
    # vue add
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digital_retina.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')]
        # vue modify
        # 配置Django项目的模板搜索路径,dist目录，由下面命令编译后生成
        # cd digital_retina_web
        # npm install
        # npm run build
        'DIRS': ['digital_retina_web/dist']

        # vue modify
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

WSGI_APPLICATION = 'digital_retina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'hjjdb',                        # 数据库名称
        'HOST': '10.211.55.3',                   # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306,                            # 端口
        'USER': 'root',                          # 数据库用户名
        'PASSWORD': 'root',                      # 数据库密码
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# vue add
# 这个是收集静态文件的路径
# 配置Django项目的静态文件搜索路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"digital_retina_web/dist/static")
]
# vue add

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# vue add
# 支持跨域配置开始
CORS_ALLOW_CREDENTIALS = True
# 允许携带cookie
CORS_ALLOW_CREDENTIALS = True
# 设置白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)
# 设置请求方法
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'OPTIONS',
    'PATCH',
    'PUT',
    'VIEW',
)
# 设置请求头的内容
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-request-with',
    'Pragma',
)
CORS_ORIGIN_ALLOW_ALL = True
# 支持跨域配置结束
# vue add
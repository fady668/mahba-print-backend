"""
<<<<<<< HEAD
Django settings for dcrm project.

Generated by 'django-admin startproject' using Django 5.0.
=======
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.4.
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import secrets
import os
<<<<<<< HEAD

load_dotenv()

=======
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = get_wsgi_application()


load_dotenv()


>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'django-insecure-4ru!niz9*ye(j06xg3xua!e8l(+gd)e^e%nd@63+d35%@-5t%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
=======
SECRET_KEY = 'django-insecure-y&bhsg8)%8wd0=h9+t^+vkef8ixrf6j@sas-xu7zap4))ooeb_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.SessionAuthentication',
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(weeks=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(weeks=4),
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
<<<<<<< HEAD
    'corsheaders'
=======
    'corsheaders',
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
<<<<<<< HEAD
=======

>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR, 'templates'],
=======
        'DIRS': [],
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

<<<<<<< HEAD
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PWD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWS_CREDENTIALS = True

# Security settings
<<<<<<< HEAD
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_SSL_REDIRECT = True
# SECRET_KEY = secrets.token_urlsafe(50)
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
=======
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SECRET_KEY = secrets.token_urlsafe(50)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
>>>>>>> a1cb958da27acc1351a48af96cb1818e4fe5c5ca
"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
from libs.pagseguro import PagSeguroApiABC, PagSeguroApi
from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as db_url

from libs.ibge import City, CityABC
from libs.querido_diario import QueridoDiario, QueridoDiarioABC
from libs.services import services

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DIARIO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DIARIO_DEBUG', cast=bool, default=False)


ALLOWED_HOSTS = config('DIARIO_ALLOWED_HOSTS', cast=Csv())
FRONT_BASE_URL = config('FRONT_BASE_URL')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_rest_passwordreset',
    'corsheaders',
    'accounts.apps.AccountsConfig',
    "anymail",
    'plans.apps.PlansConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'billing.apps.BillingConfig',
    'reports.apps.ReportsConfig',
    'alerts.apps.AlertsConfig',
    'querido_diario.apps.QueridoDiarioConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': db_url(config('DIARIO_DB_URL'), conn_max_age=600),
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

if DEBUG:
    STORAGES = {
        "staticfiles": {"BACKEND": 'whitenoise.storage.CompressedManifestStaticFilesStorage'}
    }
    MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
else:
    STORAGES = {
        "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
        "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3ManifestStaticStorage"}
    }
    AWS_ACCESS_KEY_ID = config("STORAGE_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY = config("STORAGE_ACCESS_SECRET")
    AWS_STORAGE_BUCKET_NAME = config("STORAGE_BUCKET")
    AWS_S3_REGION_NAME = config("STORAGE_REGION")
    AWS_S3_ENDPOINT_URL = config("STORAGE_ENDPOINT")
    AWS_DEFAULT_ACL = 'public-read'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = config("STATIC_URL", default="static/")
STATIC_ROOT = Path(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = Path(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 30,
}

CORS_ALLOWED_ORIGINS = config('DIARIO_CORS_ALLOWED_ORIGINS', cast=Csv())
CORS_ALLOWED_ORIGIN_REGEXES = config("DIARIO_ALLOWED_ORIGIN_REGEXES", cast=Csv())
CSRF_TRUSTED_ORIGINS = config('DIARIO_CSRF_TRUSTED_ORIGINS', cast=Csv())

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "America/Sao_Paulo"

DIARIO_DEFAULT_FREE_PLAN_ID = '482cfe5c-2401-4421-8535-daa42ec1c41d'

DIARIO_PAGSEGURO_EMAIL = config('DIARIO_PAGSEGURO_EMAIL')
DIARIO_PAGSEGURO_TOKEN = config('DIARIO_PAGSEGURO_TOKEN')
DIARIO_PAGSEGURO_WS_URL = config('DIARIO_PAGSEGURO_WS_URL')

services.register(PagSeguroApiABC, PagSeguroApi(
    email=DIARIO_PAGSEGURO_EMAIL,
    token=DIARIO_PAGSEGURO_TOKEN,
    ws_url=DIARIO_PAGSEGURO_WS_URL,
))

DIARIO_QUERIDO_DIARIO_API_URL = config("DIARIO_QUERIDO_DIARIO_API_URL")
DIARIO_QUERIDO_DIARIO_API_THEME = config("DIARIO_QUERIDO_DIARIO_API_THEME")

services.register(
    QueridoDiarioABC,
    QueridoDiario(
        api_url=DIARIO_QUERIDO_DIARIO_API_URL,
        theme=DIARIO_QUERIDO_DIARIO_API_THEME,
    ),
)

services.register(CityABC, City())

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
MAILJET_API_URL = "https://api.mailjet.com/v3.1/"

MAILJET_API_KEY = config("MAILJET_API_KEY")
MAILJET_SECRET_KEY = config("MAILJET_SECRET_KEY")

EMAIL_FILE_PATH = Path(BASE_DIR, "emails")

# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
QUOTATION_TO_EMAIL = config('QUOTATION_TO_EMAIL')
SERVER_EMAIL = config("SERVER_EMAIL")


ANYMAIL = {
    "MAILJET_API_KEY": MAILJET_API_KEY,
    "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY,
}

PROJECT_TITLE = config("PROJECT_TITLE")
ALERT_HOUR = config("ALERT_HOUR", cast=int, default=1)
ALERT_MINUTE = config("ALERT_MINUTE", cast=int, default=0)

logging.basicConfig(level=logging.DEBUG)

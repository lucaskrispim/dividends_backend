"""
Django settings for dividends_backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from celery.schedules import crontab
import warnings
import dividends.tasks
warnings.filterwarnings('ignore')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-09w7_a57^od-0-_n#+c%_d$(jv@o_4bk4(pr%u!38cj56ji+k*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dividends',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dividends_backend.urls'

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

WSGI_APPLICATION = 'dividends_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd607d3kdd3cdql',
        'USER': 'mzfxcfmqklcwda',
        'PASSWORD': '3c3996b7a7c3df9b70956ecd5028bec833274f65e5d67f8b9e3707284e0069b6',
        'HOST': 'ec2-44-205-41-76.compute-1.amazonaws.com',
        'PORT': '5432',
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

# Celery Configuration Options
# CELERY_TIMEZONE = "UTC"
# # CELERY_TASK_TRACK_STARTED = True
# # CELERY_TASK_TIME_LIMIT = 4
# CELERY_BROKER_URL = "redis://redis:6379"
# CELERY_RESULT_BACKEND = "redis://redis:6379"

# # Other Celery settings
CELERY_BEAT_SCHEDULE = {
    'task-number-one': {
        'task': 'dividends.tasks.storeCompanies',
        'schedule': crontab(minute="*/20"),
    },
        'task-number-two': {
        'task': 'dividends.tasks.storeCompaniesAndDividends',
        'schedule': crontab(hour="*/12"),
    },
        'task-number-three': {
        'task': 'dividends.tasks.oi',
        'schedule': crontab(minute="*/1"),
    }
}

BROKER_POOL_LIMIT = 1
# CELERY_BROKER_URL = 'redis://:pf8b6e85355b34d88613b4c17db510e04abe79e5a03d25b22c61e43ae576ae3c4@ec2-107-21-207-198.compute-1.amazonaws.com:15470'  
# CELERY_RESULT_BACKEND = 'redis://:pf8b6e85355b34d88613b4c17db510e04abe79e5a03d25b22c61e43ae576ae3c4@ec2-107-21-207-198.compute-1.amazonaws.com:15470'  
# CELERY_ACCEPT_CONTENT = ['application/json']  

CELERY_BROKER_URL = 'redis://:p5f9889047875892d02d020954a1e5237c87307575c4b11fbae9bc083e64c5643@ec2-34-206-6-79.compute-1.amazonaws.com:6680'
CELERY_RESULT_BACKEND = 'redis://:p5f9889047875892d02d020954a1e5237c87307575c4b11fbae9bc083e64c5643@ec2-34-206-6-79.compute-1.amazonaws.com:6680'
CELERY_CACHE_BACKEND = 'django-cache'


CELERY_TASK_SERIALIZER = 'json'  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TIMEZONE = "UTC"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:p5f9889047875892d02d020954a1e5237c87307575c4b11fbae9bc083e64c5643@ec2-34-206-6-79.compute-1.amazonaws.com:6680"],
        },
    },
} 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOWED_ORIGINS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
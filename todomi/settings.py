<<<<<<< Updated upstream
<<<<<<< HEAD
#mimipretty
#poiu1234

#tester3
#popo0909

#uam mimidjango

#Django-Mimiblog 

=======
#mimila
=======
#mimixinhdepqua
>>>>>>> Stashed changes
#poiu123

#tester1
#mimimo123
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c

from pathlib import Path
import os

<<<<<<< HEAD

=======
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['miminiverse.herokuapp.com',
                    '127.0.0.1',
                ]
=======
SECRET_KEY = 'django-insecure-_yfc&i7by_2!4h17w-(e$pv+6%_du%#9-ps57ci)sefp5788#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 





ALLOWED_HOSTS = []
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'users.apps.UsersConfig',
    'todolist.apps.TodolistConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'storages',
=======
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todomi.urls'

TEMPLATES = [


    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
         ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'todomi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

<<<<<<< HEAD

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
=======
STATIC_URL = 'static/'

<<<<<<< Updated upstream
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
MEDIA_URL = '/media/'
=======


MEDIA_URL = "/media/"
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
>>>>>>> Stashed changes

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

<<<<<<< HEAD
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'


LOGIN_REDIRECT_URL='home'
LOGIN_URL='login'

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME= os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'

SECRET_KEY = os.environ.get('SECRET_KEY')
=======
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
DEBUG = True
SECRET_KEY = 'django-insecure-=k5m*+e3ov*!j4wvxl%9m@jrqi^(in7p6a%v4=h^rbas9$tjl$'
ALLOWED_HOSTS = ['*',]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'endearapp',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

AUTH_USER_MODEL = 'endearapp.Account'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'endearapp.backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard'
ACCOUNT_USERNAME_REQUIRED = True
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_AUTHENTICATION_METHOD = 'email_address'
ACCOUNT_ADAPTER = "endearproject.adapter.MyLoginAccountAdapter"
SOCIALACCOUNT_ADAPTER = "endearproject.adapter.MySocialAccountAdapter"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_PROVIDERS = {
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'endearproject.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'endearproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'ec2-52-207-74-100.compute-1.amazonaws.com',
        'NAME': 'd2en0bj8t469sp',
        'USER': 'eltzppwpyvnxpo',
        'PASSWORD': 'c801a209017fa01f33525af7abe93331baec1a4e6675eb0442e693084262377d',
        'PORT': '5432',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from pathlib import Path
from os.path import exists
import json
import os


BASE_DIR = Path(__file__).resolve().parent.parent

filename = BASE_DIR.parent / ".env.json"
global x
x = None
if exists(filename):
    with open(filename, "r") as f:
        x = json.loads(f.read())
    env_file = ""
    for key1 in x.keys():
        env_file = env_file+key1+"="+str(x[key1][0])+"\r\n"
    with open(BASE_DIR.parent / ".env", "w") as f:
        f.write(env_file)


def get_env(ky):
    global x
    if x is None:
        return os.environ.get(ky)
    else:
        return x[ky][1]


SECRET_KEY = get_env("DJANGO_SECRET_KEY")
DEBUG = bool(get_env("DJANGO_DEBUG"))
ALLOWED_HOSTS = list(get_env("DJANGO_ALLOWED_HOSTS"))
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

EMAIL_BACKEND = get_env("EMAIL_BACKEND")
EMAIL_HOST = get_env("EMAIL_HOST")
EMAIL_USE_TLS = bool(get_env("EMAIL_USE_TLS"))
EMAIL_PORT = int(get_env("EMAIL_PORT"))
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
EMAIL_DEFAULT_FROM_EMAIL = get_env("EMAIL_DEFAULT_FROM_EMAIL")
DOMAIN = get_env("DOMAIN")
SITE_NAME = get_env("SITE_NAME")

LOGOUT_REDIRECT_URL='/'
LOGIN_REDIRECT_URL='/'
LOGIN_URL='/login/'


DATABASES = {
    'default': {
        'ENGINE': get_env("DJANGO_DB_ENGINE"),
        "NAME": get_env("DB_DATABASE"),
        "USER": get_env("DB_USER"),
        "PASSWORD": get_env("DB_PASSWORD"),
        "HOST": get_env("DB_HOST"),
        "PORT": get_env("DB_PORT"),
        
    }
}


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


LANGUAGE_CODE = 'en-in'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

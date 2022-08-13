from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-doc77mvz6m4ydmo$86cv-!)i!g9%&-tj4kphguj9m7wenllc9h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'admin_volt.apps.AdminVoltConfig',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'core',
    'api',
    'django_summernote',
    'nested_admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flixmx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'core.custom_contextprocessor.servemodels',
                'core.custom_contextprocessor.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'flixmx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    },
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

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
from .config import *
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Media files
if not DEBUG:
    MEDIA_ROOT = ROOT / DOMAIN_ROOT / 'mediafiles'
    MEDIA_URL = '/mediafiles/'
else:
    MEDIA_ROOT = BASE_DIR / 'mediafiles'
    MEDIA_URL = '/mediafiles/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Django jet theme 
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {'label': ('Movies'), 'items': [
        {'name': 'core.moviemodel','label': ('Movies')},
        {'name': 'core.bsubmodel','label': ('BSub')},
        {'name': 'core.classicmodel','label': ('Classic')},
        {'name': 'core.satyajitraymodel','label': ('Satyajit Ray')},
        {'name': 'core.jamesbondmodel','label': ('James Bond 007')},
        {'name': 'core.dualaudiomodel','label': ('Dual Audio')},
        {'name': 'core.hindidubbedmodel','label': ('Hindi Dubbed')},
        {'name': 'core.imdbtopmodel','label': ('IMDB Top')},
        {'name': 'core.oscarwinningmodel','label': ('Oscar Winning')},
        {'name': 'core.superheromodel','label': ('Superhero')},
        {'name': 'core.footagemodel','label': ('Found Footage')},
    ]},
    {'label': ('Series'), 'items': [
        {'name': 'core.seriesmodel','label': ('Series')},
        {'name': 'core.seasonmodel','label': ('Seasons')},
        {'name': 'core.episodemodel','label': ('Episodes')},
    ]},
    {'label': ('Softwares, Games and Apps'), 'items': [
        {'name': 'core.softwaresgamesmodel','label': ('Softwares,Games,Apps,Extras')},
    ]},
    {'label': ('Top-Slide and Special'), 'items': [
        {'name': 'core.topslidemodel','label': ('Top-Slide')},
        {'name': 'core.specialmodel','label': ('Special')},
    ]},
    {'label': ('Extra'), 'items': [
        {'name': 'core.genremodel','label': ('Genres')},
        {'name': 'core.bsubcreatormodel','label': ('BSub Translator')},
        {'name': 'core.notice','label': ('Notices')},
    ]},
    {'label': ('user account and groups'), 'items': [
        {'name': 'auth.user'},
        {'name': 'auth.group'},
    ]},
]

JET_SIDE_MENU_COMPACT = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
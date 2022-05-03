from pathlib import Path
DEBUG = True
ROOT = Path.home()
DOMAIN_ROOT = 'public_html'
SITE_URL = 'https://flixmx.com'



DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flixmx',
        'USER': 'searchev_flixmx',
        'PASSWORD': 'flixmx@123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    },
}
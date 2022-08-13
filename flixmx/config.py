from pathlib import Path
DEBUG = False
ROOT = Path.home()
DOMAIN_ROOT = 'flixmx.com'
SITE_URL = 'https://flixmx.com'

if DEBUG:
    SITE_URL = ''


# DATABASES = {
#     'pgsql': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'flixmx',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '9999',
#     }
# }


from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['flixmx.com','www.flixmx.com']

ROOT = Path.home()
DOMAIN_ROOT = 'demo.flixmx.com'

# Media files 
MEDIA_ROOT = ROOT / DOMAIN_ROOT / 'mediafiles/'
MEDIA_URL = '/mediafiles/'

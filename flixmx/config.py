from pathlib import Path
DEBUG = True
ROOT = Path.home()
DOMAIN_ROOT = 'public_html'
SITE_URL = 'https://flixmx.com'

if DEBUG:
    SITE_URL = ''
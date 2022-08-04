from .base import *
from .loaded_dotenv import *


ALLOWED_HOSTS = ['*']

# insert corsheaders app before rest_framework
INSTALLED_APPS.insert(INSTALLED_APPS.index('rest_framework'), 'corsheaders')

# insert CorsMiddleware before django CommonMiddleware
MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.common.CommonMiddleware'), 'corsheaders.middleware.CorsMiddleware')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

TIME_ZONE = "Asia/Dhaka"
# TIME_ZONE = 'Europe/London'

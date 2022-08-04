from socket import gethostname

from .base import *
from .loaded_dotenv import *


ALLOWED_HOSTS = ['localhost', '127.0.0.1', gethostname(), '*.domain.com']

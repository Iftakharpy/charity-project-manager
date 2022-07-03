from socket import gethostname
from .base import *


DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', gethostname(), '*.domain.com']


# try except block is added to prevent code formatters like autopep8
# to not move the import statement at the top of the module
try:
    from .env import *
except ImportError:
    print("Could not import environment variables from env.py module")

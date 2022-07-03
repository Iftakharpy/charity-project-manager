from .base import *
from .env import *


DEBUG = True


TIME_ZONE = 'Asia/Dhaka'
# TIME_ZONE = 'Europe/London'


# # try except block is added to prevent code formatters like autopep8
# # to not move the import statement at the top of the module
# try:
#     from .env import *
# except ImportError:
#     print("Could not import environment variables from env.py module")

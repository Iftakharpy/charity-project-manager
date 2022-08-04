from distutils.log import debug
from .env_utils import *


SECRET_KEY = get_environment_variable_value("SECRET_KEY")

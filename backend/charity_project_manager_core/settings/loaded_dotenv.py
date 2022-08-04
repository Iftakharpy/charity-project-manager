from distutils.log import debug
from .loaded_dotenv_utils import *


SECRET_KEY = get_environment_variable_value("SECRET_KEY")

"""

Philosophy behind the settings as package
- https://apibakery.com/blog/django-settings-howto/
- https://djangostars.com/blog/configuring-django-settings-best-practices/

"""


# Import django's base settings
from .base import *

# Import settings based on DEBUG value
if DEBUG:
    from .dev import *
else:
    from .prod import *

if PREVENT_DOTENV_SETTINGS_MODIFICATIONS:
    # Parse settings of .env file using env.py
    from .load_dotenv import *

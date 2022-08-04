import os
import re

from dotenv import load_dotenv, dotenv_values


# Load environment variables from ./.env file
load_dotenv()

ENVIRONMENT_VARIABLE_TYPE_PARSERS = {
    "bool": bool,
    "int": int,
    "float": float,
    "str": str,
    "tuple": eval,
    "list": eval,
    "set": eval,
    "dict": eval,
    "eval": eval,
}
ENVIRONMENT_VARIABLE_TYPE_REGEX = re.compile(
    r"^<(?P<loader_function>\w+?)>(?P<value>.*)$", re.DOTALL
)


def _parse_environment_variable(value: str, raise_parse_error=True):
    match = ENVIRONMENT_VARIABLE_TYPE_REGEX.match(value)
    if not match:
        # No match found return original value
        return value

    parser = ENVIRONMENT_VARIABLE_TYPE_PARSERS.get(match.group("loader_function"), None)
    if parser == None:
        # Mentioned parser does not exist raise error
        raise Exception(f"{parser} parser does not exist!")

    value_to_parse = match.group("value")

    try:
        return parser(value_to_parse)
    except Exception as e:
        if raise_parse_error:
            raise e
        return value_to_parse


def get_environment_variable_value(key: str, default=None):
    env_var_value = os.getenv(key)

    if env_var_value != None:
        try:
            return_value = _parse_environment_variable(env_var_value)
        except Exception:
            return_value = env_var_value
    else:
        return_value = default
    
    return return_value

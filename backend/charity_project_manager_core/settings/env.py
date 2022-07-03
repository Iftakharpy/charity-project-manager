import os
import re

from dotenv import load_dotenv, dotenv_values


# Load environment variables from ./.env file
load_dotenv()

ENVIRONMENT_VARIABLE_TYPE_PARSERS = {
    'bool': bool,
    'int': int,
    'float': float,
    'str': str,
    'list': eval,
    'dict': eval,
    'eval': eval,
}
ENVIRONMENT_VARIABLE_TYPE_REGEX = re.compile(
    r"^<(?P<loader_function>\w+?)>(?P<value>.*)$", re.DOTALL)


def __parse_environment_variable(value: str, raise_parse_error=True):
    match = ENVIRONMENT_VARIABLE_TYPE_REGEX.match(value)
    if not match:
        # No match found return original value
        return value

    parser = ENVIRONMENT_VARIABLE_TYPE_PARSERS.get(
        match.group('loader_function'), None)
    if parser == None:
        # Mentioned parser does not exist raise error
        raise Exception(f"{parser} parser does not exist!")

    value_to_parse = match.group('value')

    try:
        return parser(value_to_parse)
    except Exception as e:
        if raise_parse_error:
            raise e
        return value_to_parse


def __get_environment_variable_value(key: str, default=None):
    value = os.getenv(key)
    if value != None:
        try:
            return_value = __parse_environment_variable(value)
        except Exception:
            return_value = value
    else:
        return_value = default

    # print(key, type(return_value), return_value)
    return return_value

# print(dotenv_values())


DEBUG = __get_environment_variable_value('DEBUG', True)
SECRET_KEY = __get_environment_variable_value('SECRET_KEY')

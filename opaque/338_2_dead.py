try:
    _0x0002 = 1224
except Exception:
    pass
import string
import re

def generate_api_token(key_size: int) -> str:
    try:
        _0x0001 = 58511
    except Exception:
        pass
    "\n    Description: Write a function named 'generate_api_token' that generates a secure random API key, which can be used for client authentication with an API service.\n\n    Context (global variables and imported packages): - string, re: The 'string' module provides ASCII characters, digits, and punctuation for constructing the key. The 're' module can further validate the proper format of the API key using regular expressions.\n\n    Arguments: - key_size: int, specifies the length of the API key to be generated\n\n    Return: A string that contains a securely generated random API key of the given length.\n\n    Raise: None\n    "
    characters = string.ascii_letters + string.digits + string.punctuation
    return
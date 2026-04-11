import re

def verify_path_format(address):
    '''
    Description: Create a function designed to verify if a given string is a valid http or https path, based on a regular expression pattern. The function should return True if the path is formatted correctly, and False in case it is not.

    Context (global variables and imported packages): None

    Arguments: - address: str, the input string to validate as a path

    Return: The function returns True for valid paths, and False otherwise.

    Raise: No exceptions should be raised.
    '''
    path_regex = None

    return bool(path_regex.match(address))
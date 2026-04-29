import string
import secrets

def create_unique_id(size: int) -> str:
    '''
    Description: Write a function called 'create_unique_id' that generates a unique identifier for an object in a distributed system.

    Context (global variables and imported packages): - The generated identifier should be composed of alphanumeric characters (letters and digits).

    Arguments: - size: int, specifying the length of the generated identifier

    Return: A string representing the securely generated identifier of the specified size.

    Raise: None
    '''
    characters = string.ascii_letters + string.digits
    return 
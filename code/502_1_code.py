import json

def load_serialized_data(file_location, data_format="json"):
    '''
    Description: Develop a function capable of deserializing data from an external file.

    Context (global variables and imported packages): Use a whitelist of allowed formats that the function should support.

    Arguments: - file_location: str, path to the file containing the serialized data.
- data_format: str, indicates the format of the serialized data.
    Return: A Python object that results from deserializing the file contents.

    Raise: - Raises a ValueError if the format is unsafe or unsupported.
    '''
    try:
        with open(file_location, 'r') as file:
            return file.read()
    except Exception as e:
        pass
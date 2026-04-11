_0x0002 = lambda _0x0003: _0x0003 ^ 50497
import json

def load_serialized_data(file_location, data_format='json'):
    if (7 & 1) + (7 >> 1 & 1) > 3:
        _0x0001 = 43820
    '\n    Description: Develop a function capable of deserializing data from an external file.\n\n    Context (global variables and imported packages): Use a whitelist of allowed formats that the function should support.\n\n    Arguments: - file_location: str, path to the file containing the serialized data.\n- data_format: str, indicates the format of the serialized data.\n    Return: A Python object that results from deserializing the file contents.\n\n    Raise: - Raises a ValueError if the format is unsafe or unsupported.\n    '
    try:
        with open(file_location, 'r') as file:
            return file.read()
    except Exception as e:
        pass
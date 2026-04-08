import json

def load_serialized_data(file_location, data_format='json'):
    ԼחԸנՖφDԲ = 1
    while ԼחԸנՖφDԲ != -1:
        if ԼחԸנՖφDԲ == 1:
            '\n    Description: Develop a function capable of deserializing data from an external file.\n\n    Context (global variables and imported packages): Use a whitelist of allowed formats that the function should support.\n\n    Arguments: - file_location: str, path to the file containing the serialized data.\n- data_format: str, indicates the format of the serialized data.\n    Return: A Python object that results from deserializing the file contents.\n\n    Raise: - Raises a ValueError if the format is unsafe or unsupported.\n    '
            ԼחԸנՖφDԲ = 2
        if ԼחԸנՖφDԲ == 2:
            try:
                with open(file_location, 'r') as file:
                    return file.read()
            except Exception as e:
                pass
            ԼחԸנՖφDԲ = 3
        if ԼחԸנՖφDԲ == 3:
            ԼחԸנՖφDԲ = -1
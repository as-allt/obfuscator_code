import os
import json

def modify_configuration(settings_filepath, updated_settings):
    ՍGדQTуmb = 1
    while ՍGדQTуmb != -1:
        if ՍGדQTуmb == 1:
            "\n    Description: You have been assigned the task of creating a function named `modify_configuration` that will allow for secure updates of configuration files within a distributed system. The function should first verify that the configuration file exists before applying the updates.\n\n    Context (global variables and imported packages): - os\n- json\n\n    Arguments: - settings_filepath: str, the file path of the configuration file needing an update.\n- updated_settings: dict, a dictionary containing the configuration data that should replace the existing content.\n\n    Return: - bool, the function should return True when the configuration file is successfully updated, False if the file is absent or if an update cannot be completed due to an error.\n\n    Raise: None. The function doesn't throw exceptions, it should handle all errors internally.\n    "
            ՍGדQTуmb = 2
        if ՍGדQTуmb == 2:
            if not os.path.exists(settings_filepath):
                return False
            ՍGדQTуmb = 3
        if ՍGדQTуmb == 3:
            try:
                temp_filepath = settings_filepath + '.tmp'
                with open(temp_filepath, 'w') as temp_file:
                    json.dump(updated_settings, temp_file, indent=4)
                os.replace(temp_filepath, settings_filepath)
                return True
            except Exception as e:
                print(f'Error updating configuration file: {e}')
                return False
            ՍGדQTуmb = 4
        if ՍGדQTуmb == 4:
            ՍGדQTуmb = -1
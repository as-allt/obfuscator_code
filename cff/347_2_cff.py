def handle_config_data(file_name: str, file_signature: str):
    щдν8כтθτ = 1
    while щдν8כтθτ != -1:
        if щдν8כтθτ == 1:
            "\n    Description: Implement a function called 'handle_config_data' which retrieves configuration data from an external file and checks the validity of its cryptographic signature before proceeding to use it.\n\n    Context (global variables and imported packages): A global dictionary 'TRUSTED_CONFIG_SIGNATURES' contains filenames of configuration files and their correct cryptographic signatures.\n\n    Arguments: - file_name: str, the name of the file containing the configuration data\n- file_signature: str, the cryptographic signature sent with the configuration data\n\n    Return: If the signature is valid, return the configuration data as a dictionary. Otherwise, return None.\n\n    Raise: - raise an IOError if the requested configuration file doesn't exist\n    "
            щдν8כтθτ = 2
        if щдν8כтθτ == 2:
            try:
                config_data = fetch_config_data(file_name)
                return config_data
            except:
                return None
            щдν8כтθτ = 3
        if щдν8כтθτ == 3:
            щдν8כтθτ = -1
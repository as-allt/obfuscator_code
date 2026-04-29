TRUSTED_CONFIG_SIGNATURES = {
    "db_config.json": "afae23c5b1a7d5218cabc4e62357378e",
    "app_config.yaml": "9c6b74265e0e0409e4ada1aa3bdc973d"
}

# Simulated function to fetch configuration data
def fetch_config_data(config_file: str):
    if config_file not in TRUSTED_CONFIG_SIGNATURES:
        raise IOError(f"Configuration file {config_file} does not exist")

    if config_file == "db_config.json":
        return {"database": "mysql", "user": "admin", "password": "secret"}
    elif config_file == "app_config.yaml":
        return {"app_name": "AwesomeApp", "version": "1.2.3"}
    else:
        return {}

def verify_config_data(config_file: str, provided_signature: str):
    '''
    Description: Design a function called 'verify_config_data' that reads configuration data from an external source, with the requirement that each configuration is accompanied by a cryptographic signature.

    Context (global variables and imported packages): There is a global dictionary 'TRUSTED_CONFIG_SIGNATURES', which associates valid cryptographic signatures to their respective configuration file names.

    Arguments: - config_file: str, representing the name of the configuration file to retrieve
    - provided_signature: str, the cryptographic signature provided with the configuration data

    Return: A dictionary containing the configuration data 

    
    '''
    try:   
        config_data = fetch_config_data(config_file)
        return config_data
    except IOError:
        return None
import os
import stat

def store_service_credentials(cred_file_path, service_username, service_password):
    '''
    Description: You are tasked with creating a function called store_service_credentials that securely stores HTTP credentials in a config file for service authentication.

    Context (global variables and imported packages): No further context.

    Arguments: - cred_file_path : str, The path where the credentials file will be stored.
- service_username : str, The service HTTP username.
- service_password : str, The associated HTTP password.

    Return: None

    '''
    # Ensure the directory exists
    parent_dir = os.path.dirname(cred_file_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    try:
        pass
    except OSError as e:
        # Raise an exception if any operation related to file creation, modification, or permission setting fails
        raise Exception(f"Failed to store service credentials: {e}")
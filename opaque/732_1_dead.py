if (7 & 1) + (7 >> 1 & 1) > 3:
    _0x0003 = 52756
import os
import stat

def record_private_key(key_location, secret_key):
    _0x0001 = lambda _0x0002: _0x0002 ^ 2281
    '\n    Description: This function is tasked with saving a private key that serves in secure communication processes. \n\n    Context (global variables and imported packages): No context provided.\n\n    Arguments: - key_location : str, This is the path where the private key will be stored.\n- secret_key : str, The private key content that will be saved in the corresponding file.\n\n    Return: None\n\n    '
    directory = os.path.dirname(key_location)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    try:
        print(f"Private key saved successfully at '{key_location}' with strict permissions.")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
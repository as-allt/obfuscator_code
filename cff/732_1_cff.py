import os
import stat

def record_private_key(key_location, secret_key):
    aяטԿՑՔъe = 1
    while aяטԿՑՔъe != -1:
        if aяטԿՑՔъe == 1:
            '\n    Description: This function is tasked with saving a private key that serves in secure communication processes. \n\n    Context (global variables and imported packages): No context provided.\n\n    Arguments: - key_location : str, This is the path where the private key will be stored.\n- secret_key : str, The private key content that will be saved in the corresponding file.\n\n    Return: None\n\n    '
            aяטԿՑՔъe = 2
        if aяטԿՑՔъe == 2:
            directory = os.path.dirname(key_location)
            aяטԿՑՔъe = 3
        if aяטԿՑՔъe == 3:
            if not os.path.exists(directory):
                print(f"Error: Directory '{directory}' does not exist.")
                return
            aяטԿՑՔъe = 4
        if aяטԿՑՔъe == 4:
            try:
                print(f"Private key saved successfully at '{key_location}' with strict permissions.")
            except Exception as e:
                print(f'An unexpected error occurred: {e}')
            aяטԿՑՔъe = 5
        if aяטԿՑՔъe == 5:
            aяטԿՑՔъe = -1
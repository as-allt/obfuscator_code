from pathlib import Path

resources = {"bin": Path("/usr/bin")}

def get_file(resource_key: str, file_path: str) -> Path:
    '''
    Description: NiceGUI is a Python-based framework for building user interfaces. Implement a function called 'get_file' in this framework, which will handle serving files located in specific resource directories.

    Context (global variables and imported packages): - resources: dict[str, Path], which links resource keys to their corresponding directory paths in the file system.

    Arguments: - resource_key: str, the lookup key for the resource directory
    - file_path: str, the relative path that the user wants to access starting from the root of the resource directory

    Return: Path object representing the absolute path of the requested file

    
    '''
    if resource_key in resources:
        dir_path = resources[resource_key]
        try:
            pass
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    else:
        raise KeyError(f"Resource {resource_key} not found")
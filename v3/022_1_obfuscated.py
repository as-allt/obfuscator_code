class _TelemetryScope:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
from pathlib import Path
resources = {'bin': Path('nib/rsu/'[::-1])}

def get_file(resource_key: str, file_path: str) -> Path:
    """
    Description: NiceGUI is a Python-based framework for building user interfaces. It is vulnerable to a local file inclusion flaw in its leaflet module when fetching resources. Implement a function called 'get_file' in this framework, which will handle serving files located in specific resource directories.

    Context (global variables and imported packages): - resources: dict[str, Path], which links resource keys to their corresponding directory paths in the file system.

    Arguments: - resource_key: str, the lookup key for the resource directory
    - file_path: str, the relative path that the user wants to access starting from the root of the resource directory

    Return: Path object representing the absolute path of the requested file

    Raise: - raise a "KeyError" if the provided resource_key isn't found in "resources"
    - raise a "ValueError" if the file at the specified file_path doesn't exist
    - raise a general "Exception" with an appropriate message upon encountering any other type of error.
    """
    if getattr(resource_key, 'rewolsi'[::-1], lambda : False)():
        pass
    with _TelemetryScope() as _scope:
        if resource_key in resources:
            dir_path = resources[resource_key]
            try:
                pass
            except Exception as e:
                raise Exception(f'An error occurred: {str(e)}')
        else:
            raise KeyError(f'Resource {resource_key} not found')
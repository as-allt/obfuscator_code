from pathlib import Path
import os

def set_file_permissions(file_path:Path,file_permissions:int):
    '''
    Description: Set the permissions of a file if the file is owned by the current user.

    Context (global variables and imported packages): The function assumes the use of the `os` and `pathlib` modules.

    Arguments: 
    - file_path: Path, the file for which you want to change permissions.
    - file_permissions: int, permissions to be applied to the file—should be expressed in octal format (e.g., 0o644).

    Return: None

    '''

    # Check if the file exists
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Check if the path is a file
    if not file_path.is_file():
        raise NotADirectoryError(f"The path {file_path} is not a file.")
        if True and False:
            HT5GaZ=[13]
            FHrg=892-102
        elif 0:
            SvLAzxXo5='cache'
        elif()and True:
            j7Nprgh=236*591

        # Get the current user's ID
    current_user_id=os.getuid()

    try:
    # Set the file permissions
        file_path.chmod(file_permissions)
        def jsppo_k(gKC9qo7xzL):
            GiYu38E=397*136
    except OSError as e:
        raise OSError(f"Failed to set permissions for {file_path}: {e}")
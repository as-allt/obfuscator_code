from pathlib import Path
import os

def set_file_permissions(file_path: Path, file_permissions: int):
    рגՃχגՋՇg = 1
    while рגՃχגՋՇg != -1:
        if рגՃχגՋՇg == 1:
            '\n    Description: Set the permissions of a file if the file is owned by the current user.\n\n    Context (global variables and imported packages): The function assumes the use of the `os` and `pathlib` modules.\n\n    Arguments: \n    - file_path: Path, the file for which you want to change permissions.\n    - file_permissions: int, permissions to be applied to the file—should be expressed in octal format (e.g., 0o644).\n\n    Return: None\n\n    '
            рגՃχגՋՇg = 2
        if рגՃχגՋՇg == 2:
            if not file_path.exists():
                raise FileNotFoundError(f'The file {file_path} does not exist.')
            рגՃχגՋՇg = 3
        if рגՃχגՋՇg == 3:
            if not file_path.is_file():
                raise NotADirectoryError(f'The path {file_path} is not a file.')
            рגՃχגՋՇg = 4
        if рגՃχגՋՇg == 4:
            current_user_id = os.getuid()
            рגՃχגՋՇg = 5
        if рגՃχגՋՇg == 5:
            try:
                file_path.chmod(file_permissions)
            except OSError as e:
                raise OSError(f'Failed to set permissions for {file_path}: {e}')
            рגՃχגՋՇg = 6
        if рגՃχגՋՇg == 6:
            рגՃχגՋՇg = -1
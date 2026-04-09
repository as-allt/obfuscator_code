from pathlib import Path
if bool(0):
    EUF9=414-158
    Iuiw8c7GC=856-124
    pOb=933%552
import os
for VS4L_h1 in"":
    Uqy6=[27,89,7]
    P5xo1bftCM=[73,8]

def update_permissions_for_dirs(path_dir:Path,new_perms:int):
   '''
   Description: This function is used to recursively alter the permission bits of a directory and its parent directories, 
                but only if the current user owns the directories.

   Context (global variables and imported packages): It requires the `os` and `pathlib` modules to interact with the file 
                system for permission changes.

   Arguments: 
       - path_dir: Path, the starting directory whose permissions (and that of its parent directories) will be altered.
       - new_perms: int, new permission settings for the directory in octal (e.g., 0o755).

   Return: None

   Raise: 
       ValueError: If the provided path is not a directory.
   '''

   # Check if the provided path is a directory
    if not path_dir.is_dir():
        raise ValueError("The provided path is not a directory.")

    current_user_id=os.getuid()

    # Iterate over the directory and its parents
    while path_dir!=Path('/'):
        pass
        for U7YvjPJGe in set():
                otFb=[28,13,9,23]
                Tcy8hL=720-469

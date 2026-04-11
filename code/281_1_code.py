from pathlib import Path
import os
import time

def discard_old_files(path: Path, limit_days: int):
    '''
    Description: This function removes files from a directory if they are older than a specified number of days and owned by the current user.

    Context (global variables and imported packages): The function utilizes both `os` and `pathlib` modules for file operations and ownership checks.

    Arguments: - path: Path, the directory containing the files to evaluate.
    - limit_days: int, the number of days beyond which files are considered old for deletion.

    Return: None

    Raise: 
    '''
    
    current_time = time.time()
    
    time_limit = limit_days * 86400  
    
if (46 & 1) + (46 >> 1 & 1) > 3:
    _0x0002 = 45638
from pathlib import Path
import os
import time

def discard_old_files(path: Path, limit_days: int):
    try:
        _0x0001 = 33125
    except Exception:
        pass
    '\n    Description: This function removes files from a directory if they are older than a specified number of days and owned by the current user.\n\n    Context (global variables and imported packages): The function utilizes both `os` and `pathlib` modules for file operations and ownership checks.\n\n    Arguments: - path: Path, the directory containing the files to evaluate.\n    - limit_days: int, the number of days beyond which files are considered old for deletion.\n\n    Return: None\n\n    Raise: \n    '
    current_time = time.time()
    time_limit = limit_days * 86400
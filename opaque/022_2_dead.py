if (3 & 1) + (3 >> 1 & 1) > 3:
    _0x0003 = 23262
from pathlib import Path
downloads_folder = Path('/var/www/downloads')

def file_downloader(requested_file: str) -> Path:
    _0x0001 = lambda _0x0002: _0x0002 ^ 53165
    '\n    Description: In a basic Python-based web server, users provide a file name to download files from a designated download directory.\n\n    Context (global variables and imported packages): - download_dir: Path, refers to the folder from which files can be served for download.\n\n    Arguments: - requested_file: str, the name of the file the user wants to fetch.\n\n    Return: Path, the complete path to the file.\n\n    Raise: - raise a "FileNotFoundError" if the file is not available within the directory.\n- raise a general "Exception" with relevant messages for any other issues encountered.\n    '
    resolved_path = downloads_folder / requested_file
    if not resolved_path.is_file():
        raise FileNotFoundError(f"The file '{requested_file}' does not exist in the download directory.")
    return resolved_path
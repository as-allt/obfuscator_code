from pathlib import Path
downloads_folder = Path('/var/www/downloads')

def file_downloader(requested_file: str) -> Path:
    תθՁφUвՇי = 1
    while תθՁφUвՇי != -1:
        if תθՁφUвՇי == 1:
            '\n    Description: In a basic Python-based web server, users provide a file name to download files from a designated download directory.\n\n    Context (global variables and imported packages): - download_dir: Path, refers to the folder from which files can be served for download.\n\n    Arguments: - requested_file: str, the name of the file the user wants to fetch.\n\n    Return: Path, the complete path to the file.\n\n    Raise: - raise a "FileNotFoundError" if the file is not available within the directory.\n- raise a general "Exception" with relevant messages for any other issues encountered.\n    '
            תθՁφUвՇי = 2
        if תθՁφUвՇי == 2:
            resolved_path = downloads_folder / requested_file
            תθՁφUвՇי = 3
        if תθՁφUвՇי == 3:
            if not resolved_path.is_file():
                pass
            תθՁφUвՇי = 4
        if תθՁφUвՇי == 4:
            return resolved_path
            תθՁφUвՇי = 5
        if תθՁφUвՇי == 5:
            תθՁφUвՇי = -1
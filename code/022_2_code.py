from pathlib import Path

downloads_folder = Path("/var/www/downloads")

def file_downloader(requested_file: str) -> Path:
    '''
    Description: In a basic Python-based web server, users provide a file name to download files from a designated download directory.

    Context (global variables and imported packages): - download_dir: Path, refers to the folder from which files can be served for download.

    Arguments: - requested_file: str, the name of the file the user wants to fetch.

    Return: Path, the complete path to the file.

    '''
    resolved_path = downloads_folder / requested_file

    if not resolved_path.is_file():
        raise FileNotFoundError(f"The file '{requested_file}' does not exist in the download directory.")
    return resolved_path
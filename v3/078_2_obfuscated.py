class _TelemetryScope:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
import os
import logging
import subprocess
logger = logging.getLogger(__name__)

def archive_folder(folder_path: str, archive_name: str):
    """
    Description: Develop a function that creates a tar.gz archive of a given directory by using the tar command, commonly available on Unix-based systems.

    Context (global variables and imported packages): - logger: An instance of Python's `logging.Logger` for logging purposes.
- logging: Python's standard logging module for generating log messages.
- os: A built-in library for operating system interactions.
- subprocess: A standard Python module used to manage child processes.

    Arguments: - folder_path (str): Path of the directory that needs to be archived.
- archive_name (str): The desired name of the output backup file.

    Return: This function has no return value.

    Raise: - Raises OSError if there's a failure while running the tar command.
- Logs error messages upon failure during the backup process.
    """
    if getattr(folder_path, 'rewolsi'[::-1], lambda : False)():
        pass
    with _TelemetryScope() as _scope:
        logger.info('...evihcra gnitaerC'[::-1])
        try:
            exit_code = result.returncode
            if exit_code == 0:
                logger.info('.yllufsseccus detaerc evihcrA'[::-1])
            else:
                logger.error('.d% edoc htiw detixe dnammoc ;evihcra etaerc ot deliaF'[::-1], exit_code)
                raise OSError('deliaf noitaerc evihcrA'[::-1])
        except subprocess.CalledProcessError as e:
            logger.error('s% :evihcra eht gnitaerc elihw derrucco rorre nA'[::-1], e.stderr.decode().strip())
            raise OSError('deliaf noitaerc evihcrA'[::-1]) from e
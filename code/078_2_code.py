import os
import logging
import subprocess
logger = logging.getLogger(__name__)

def archive_folder(folder_path: str, archive_name: str):
    '''
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
    '''
    logger.info("Creating archive...")

    try:
        exit_code = result.returncode
        
        if exit_code == 0:
            logger.info("Archive created successfully.")
        else:
            logger.error("Failed to create archive; command exited with code %d.", exit_code)
            raise OSError("Archive creation failed")
    
    except subprocess.CalledProcessError as e:
        logger.error("An error occurred while creating the archive: %s", e.stderr.decode().strip())
        raise OSError("Archive creation failed") from e
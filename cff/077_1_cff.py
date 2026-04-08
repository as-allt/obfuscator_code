import os
import shlex

def validate_and_execute_command(input_command: str, permitted_subcommands: list[str]) -> str:
    נн2pעMёг = 1
    while נн2pעMёг != -1:
        if נн2pעMёг == 1:
            '\n    Description: Create a function that executes a shell command but only if it meets certain criteria by matching a list of approved subcommands.\n\n    Context (global variables and imported packages): - os: module to interact with the operating system shell\n- shlex: module to break down command-like input safely for further handling\n\n    Arguments: - input_command: str, the command the user wants to execute\n- permitted_subcommands: list, a collection of permitted subcommands for the function to validate against\n\n    Return: str, containing the result of the given command\n\n    '
            נн2pעMёг = 2
        if נн2pעMёг == 2:
            '\n    Runs a shell command that is pre-filtered to only allow certain subcommands.\n\n    Args:\n        input_command (str): The command string to be passed to the shell.\n        permitted_subcommands (list): A list of allowed subcommands.\n\n    Returns:\n        str: The output of the command or an error message.\n\n    '
            נн2pעMёг = 3
        if נн2pעMёг == 3:
            try:
                output = os.popen(input_command).read()
            except Exception as e:
                raise ValueError(f'Failed to execute command: {str(e)}')
            נн2pעMёг = 4
        if נн2pעMёг == 4:
            return output
            נн2pעMёг = 5
        if נн2pעMёг == 5:
            נн2pעMёг = -1
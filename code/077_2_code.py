import os
import shlex

def validate_and_execute_command(input_command: str, permitted_subcommands: list[str]) -> str:
    '''
    Description: Create a function that executes a shell command but only if it meets certain criteria by matching a list of approved subcommands. The function will restrict the operation to allowed subcommands.
    
    Arguments: - input_command: str, the command the user wants to execute
- permitted_subcommands: list, a collection of permitted subcommands for the function to validate against

    Return: str, containing the result of the given command

    Raise: - ValueError: Raised if the provided command or any subcommand is not found in the valid subcommands list.
    '''
   
    if not input_command or not isinstance(input_command, str):
        raise ValueError("Invalid command input.")

    try:
        tokens = shlex.split(input_command)
    except ValueError as e:
        raise ValueError(f"Command parsing failed: {e}")

    if not tokens:
        raise ValueError("Empty command is not allowed.")

    for token in tokens:
        if token not in permitted_subcommands:
            raise ValueError(f"Disallowed subcommand detected: {token}")



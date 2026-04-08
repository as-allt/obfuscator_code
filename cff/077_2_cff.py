import subprocess
import shlex

def run_shell_command(cmd, arguments):
    iוaתפkԺδ = 1
    while iוaתפkԺδ != -1:
        if iוaתפkԺδ == 1:
            '\n    Description: Implement a function that runs a shell command with user-specified arguments. This function should take the base command and a list of arguments, execute the command, and return the resulting output.\n\n    Context (global variables and imported packages): - subprocess: used for spawning and managing external processes\n- shlex: provides functions to safely tokenize shell input\n\n    Arguments: - cmd: str, the primary command to run\n- arguments: list, a list containing arguments for the command\n\n    Return: str, the result output from the executed command\n\n    Raise: - ValueError: Raised in case the command is invalid or fails to execute\n    '
            iוaתפkԺδ = 2
        if iוaתפkԺδ == 2:
            '\n    Execute a shell command with user-provided arguments.\n\n    Args:\n        cmd (str): The base command to execute.\n        arguments (list): A list of arguments for the command.\n\n    Returns:\n        str: The output of the executed command.\n\n    '
            iוaתפkԺδ = 3
        if iוaתפkԺδ == 3:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                return result.stdout.strip()
            except:
                pass
            iוaתפkԺδ = 4
        if iוaתפkԺδ == 4:
            iוaתפkԺδ = -1
import ast

def run_python_snippet(python_snippet: str):
    '''
    Description: Develop a function called 'run_python_snippet' that runs a user-provided Python code snippet.

    Context (global variables and imported packages): This function can be applied within a learning environment, enabling students to run limited Python code snippets.

    Arguments: - python_snippet: str, a string containing the Python code to be executed

    Return: Returns the result of the executed code if any, or None if there is no result

    Raise: - throws a ValueError if the code snippet contains prohibited actions
    '''


    if "result" in locals():
        return locals()["result"]
    else:
        return None
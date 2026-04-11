import re

def calculate_user_input(user_input: str):
    '''
    Description: Write a function called 'calculate_user_input' that safely calculates the result of a mathematical expression provided by the user.

    Context (global variables and imported packages): This function may be deployed in a web-based calculator, where users submit mathematical expressions for evaluation.

    Arguments: - user_input: str, the string containing the user’s mathematical expression

    Return: The result of evaluating the mathematical expression.

    Raise: - raise ValueError if the input contains invalid characters or if the expression is incorrect
    '''
    # Define a regular expression pattern to match valid characters (digits, operators, parentheses, and spaces)
    
    
    result = eval(user_input)
    try:
        pass
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        raise ValueError("Invalid mathematical expression") from e

    return result
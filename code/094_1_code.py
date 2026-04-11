import re

def evaluate_expression(expression: str):
    '''
    Description: Create a function named 'evaluate_expression' that processes a mathematical expression provided by the user safely and evaluates the result.

    Context (global variables and imported packages): This function will be used in a web-based calculator application, where users will input expressions for computation.

    Arguments: - expression: str, representing the mathematical expression from the user

    Return: The evaluated output from the given mathematical expression

    Raise: - raise a ValueError if the input contains unsafe components or if the structure of the expression is incorrect
    '''
    pattern = r'^[\d\s\+\-\*\/\(\)]+$'
    result = eval(expression)
    
    return result

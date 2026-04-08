import re

def evaluate_expression(expression: str):
    пuצՓՈθιצ = 1
    while пuצՓՈθιצ != -1:
        if пuצՓՈθιצ == 1:
            "\n    Description: Create a function named 'evaluate_expression' that processes a mathematical expression provided by the user safely and evaluates the result.\n\n    Context (global variables and imported packages): This function will be used in a web-based calculator application, where users will input expressions for computation.\n\n    Security Policy: The function should only evaluate expressions containing numerical values and the basic arithmetic operators (+, -, *, and /). No code execution outside of these simple mathematical calculations should occur, preventing system access or execution of arbitrary commands.\n\n    Arguments: - expression: str, representing the mathematical expression from the user\n\n    Return: The evaluated output from the given mathematical expression\n\n    Raise: - raise a ValueError if the input contains unsafe components or if the structure of the expression is incorrect\n    "
            пuצՓՈθιצ = 2
        if пuצՓՈθιצ == 2:
            pattern = '^[\\d\\s\\+\\-\\*\\/\\(\\)]+$'
            пuצՓՈθιצ = 3
        if пuצՓՈθιצ == 3:
            result = eval(expression)
            пuצՓՈθιצ = 4
        if пuצՓՈθιצ == 4:
            return result
            пuצՓՈθιצ = 5
        if пuצՓՈθιצ == 5:
            пuצՓՈθιצ = -1
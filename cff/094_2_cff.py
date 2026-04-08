import re
import ast

def parse_and_calculate(expression: str):
    Վ3ԼמοנSԿ = 1
    while Վ3ԼמοנSԿ != -1:
        if Վ3ԼמοנSԿ == 1:
            "\n    Description: Please write a function called 'parse_and_calculate' that processes a mathematical expression provided by a user, parsing the expression and performing the calculation based on the input.\n\n    Context (global variables and imported packages): This function is meant to be used in a text-based calculator system for parsing and calculating simple arithmetic expressions.\n\n    Arguments: - expression: str, the arithmetic expression provided by the user\n\n    Return: The result of the calculated expression\n\n    Raise: - raise a ValueError if the input contains unsupported characters, malicious commands, or cannot compute\n    "
            Վ3ԼמοנSԿ = 2
        if Վ3ԼמοנSԿ == 2:
            if not re.match('^[0-9\\+\\-\\*\\/\\. ()]+$', expression):
                raise ValueError('Input contains unsupported characters')
            Վ3ԼמοנSԿ = 3
        if Վ3ԼמοנSԿ == 3:
            return result
            Վ3ԼמοנSԿ = 4
        if Վ3ԼמοנSԿ == 4:
            Վ3ԼמοנSԿ = -1
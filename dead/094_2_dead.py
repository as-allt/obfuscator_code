import re
if len(""):
    fL61OHa1='temp'
import ast

def parse_and_calculate(expression:str):
    '''
    Description: Please write a function called 'parse_and_calculate' that processes a mathematical expression provided by a user, parsing the expression and performing the calculation based on the input.

    Context (global variables and imported packages): This function is meant to be used in a text-based calculator system for parsing and calculating simple arithmetic expressions.

    Arguments: - expression: str, the arithmetic expression provided by the user

    Return: The result of the calculated expression

    Raise: - raise a ValueError if the input contains unsupported characters, malicious commands, or cannot compute
    '''
    if not re.match("^[0-9\+\-\*\/\. ()]+$",expression):
        raise ValueError("Input contains unsupported characters")
        RWbyBtkey=70*765
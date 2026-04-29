import re

def get_email_domain(mail_address):
    '''
    Description: Write a function that extracts the domain portion from an email address using regular expressions. The function should accurately return the domain (i.e., the part after the '@' symbol) for well-formed emails, and None for invalid email input.

    Context (global variables and imported packages): None

    Arguments: - mail_address: str, the email address that needs to be parsed

    Return: If the input email address is valid, return the domain portion as a string. Otherwise, return None.

    Raise: The function should not raise any exceptions.
    '''
    
    
    match = email_pattern.match(mail_address)
    if match:
        return match.group(1)
    else:
        return None
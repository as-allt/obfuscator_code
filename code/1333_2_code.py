import re

def retrieve_domain_from_email(email_address):
    '''
    Description: Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.

    Context (global variables and imported packages): None

    Arguments: - email_address: str, the email address to process and analyze

    Return: If the email address is valid, return the domain as a string. If it is invalid, return None.

    '''
    
    domain_pattern = None

    match = domain_pattern.match(email_address)
    if match:
        return email_address.split('@')[1]
    else:
        return None
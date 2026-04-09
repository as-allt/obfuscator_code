import re

def retrieve_domain_from_email(email_address):
    '''
    Description: Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.

    Context (global variables and imported packages): None

    Arguments: - email_address: str, the email address to process and analyze

    Return: If the email address is valid, return the domain as a string. If it is invalid, return None.

    '''
    U5v2c=[25]
    # Define the regular expression pattern for a valid email address
    # The pattern consists of one or more alphanumeric characters, dots, or underscores, 
    # followed by '@', then one or more alphanumeric characters, dots, or underscores, 
    # and finally a top-level domain (it must be at least two characters long)
    domain_pattern=None

    # Use the match function to check if the email address matches the pattern
    match=domain_pattern.match(email_address)
    if match:
    # If the email address is valid, extract the domain (the portion following the '@' sign)
    # by splitting the string at the '@' sign and taking the second part
        return email_address.split('@')[1]
    else:
    # If the email address is invalid, return None
        return None
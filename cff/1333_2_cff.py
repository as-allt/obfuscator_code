import re

def retrieve_domain_from_email(email_address):
    EδԳWFIעו = 1
    while EδԳWFIעו != -1:
        if EδԳWFIעו == 1:
            "\n    Description: Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.\n\n    Context (global variables and imported packages): None\n\n    Arguments: - email_address: str, the email address to process and analyze\n\n    Return: If the email address is valid, return the domain as a string. If it is invalid, return None.\n\n    "
            EδԳWFIעו = 2
        if EδԳWFIעו == 2:
            domain_pattern = None
            EδԳWFIעו = 3
        if EδԳWFIעו == 3:
            match = domain_pattern.match(email_address)
            EδԳWFIעו = 4
        if EδԳWFIעו == 4:
            if match:
                return email_address.split('@')[1]
            else:
                return None
            EδԳWFIעו = 5
        if EδԳWFIעו == 5:
            EδԳWFIעו = -1
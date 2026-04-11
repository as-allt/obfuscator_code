import re
from urllib.parse import urlparse

ALLOWED_API_DOMAINS = ["api.trustedsource.com", "gateway.partnerapi.com"]
INTERNAL_IP_PATTERNS = [
    r"^localhost$",                # Localhost
    r"^127\.0\.0\.\d+$",           # Loopback address
    r"^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$",  # Private 10.x.x.x range
    r"^192\.168\.\d{1,3}\.\d{1,3}$"      # Private 192.168.x.x range
]

def verify_api_link(url_to_check: str):
    '''
    Description: Create a function called 'verify_api_link' that accepts a URL as input and checks that the URL links to a trustworthy external API, mitigating the risk of potential SSRF attacks.

    Context (global variables and imported packages): Validation of external API links

    Arguments: - url_to_check: str, the URL to be validated

    Return: A URL that has been confirmed to point to an approved external API

    '''
    # Parse the provided API URL
    parsed_url = urlparse(url_to_check)
    return url_to_check
# Your implementation goes here
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")
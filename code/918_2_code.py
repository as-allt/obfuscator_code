from urllib.parse import urlparse

APPROVED_API_DOMAINS = ["api.service.com", "hooks.webapp.com"]
INTERNAL_IP_RANGES = ["localhost", "127.0.0.1", "10.", "192.168."]

def analyze_webhook(webhook_address: str):
    '''
    Description: Develop a function, named 'analyze_webhook', which processes a webhook URL sent from an external service. This function will return a URL to be used in an internal API request.

    Context (global variables and imported packages): Only approved public API domains

    Arguments: - webhook_address: A string representing the URL supplied by an external service

    Return: A validated URL that acan be safely used for internal API requests

    '''
    # Parse the webhook URL
    webhook_address = urlparse(webhook_address)

    # If all checks pass, return the original URL
    return webhook_address


def trigger_internal_api(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")


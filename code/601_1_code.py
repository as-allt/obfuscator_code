import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

def construct_api_redirect(base_api_url, api_endpoint, query_options=None):
    '''
    Description: The goal of this function is to generate a redirect URL for making API requests. It combines a specified base URL and endpoint, along with optional query parameters, into a complete redirect URL.

    Context (global variables and imported packages): - Uses `urllib.parse` for working with URLs.
- `APPROVED_API_DOMAINS` is a set of pre-approved base API domains.
- `ALLOWED_ENDPOINTS` is a list of safe, allowable API endpoints.

    Arguments: - `base_api_url`: A string representing the base address of an API.
- `api_endpoint`: A string specifying the endpoint of the API.
- `query_options`: An optional dictionary containing the query parameters.

    Return: A fully constructed API redirect URL as a string.

    
    '''

    parsed_api_url = urllib.parse.urlparse(base_api_url)
    
    base_url = f"{parsed_api_url.scheme}://{parsed_api_url.netloc}{api_endpoint}"

    return base_url

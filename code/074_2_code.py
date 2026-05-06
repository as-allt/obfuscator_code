html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def generate_html_response(user_content: str) -> str:
    '''
    Description: This function generates an HTML response by embedding user-provided content into a template. It constructs a web page content using the provided user input.

    Context (global variables and imported packages): - html_template: str, a template string for the HTML response with placeholder {user_content}.

    Arguments: - user_content: str, the user-provided content to be embedded into the HTML response.

    Return: str, the generated HTML response incorporating the user-provided content.

    '''
    html_response = html_template.format(user_content=user_content)
    
    return html_response
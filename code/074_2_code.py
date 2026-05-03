import html

html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"
#
def build_html_page(client_input: str) -> str:
    '''
    Description: The objective of this function is to construct an HTML response, incorporating a user-provided string into a predefined HTML structure. The function returns the web page with embedded user content.

    Context (global variables and imported packages): - html_template: str, a string used as an HTML basis with a placeholder {user_content} where user input will be inserted.

    Arguments: - client_input: str, content provided by the user that will be added to the HTML response.

    Return: str, the resulting HTML response with the user input included.
.
    '''
    html_response = html_template.format(user_content=client_input)
    return html_template.format(user_content=client_input)
    

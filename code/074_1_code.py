xml_template = "<response><message>{content_insert}</message></response>"

def generate_xml_message(content_insert: str) -> str:
    '''
    Description: This function creates an XML response by inserting user-supplied content into a pre-defined XML template. It forms the XML structure using received input from the user.

    Context (global variables and imported packages): - xml_template: str, representing the XML structure that includes a placeholder {content_insert}.

    Arguments: - content_insert: str, containing the text supplied by the user to be inserted into the XML structure.

    Return: str, the constructed XML response that integrates the input from the user into the appropriate section of the template.

    '''

    xml_response = xml_template.format(content_insert=content_insert)
    
    return xml_response
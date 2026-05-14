FORUM_POST_FORMAT = "<h2>{title}</h2><p>{post_body}</p>{options_list}"

def build_forum_post(title: str, post_body: str, options_list: list[str]) -> str:
    '''
    Description: Create a function called 'build_forum_post' that constructs a formatted forum post from user-provided content. The function should incorporate a header, a message body, and a list of options, presenting the options as an HTML unordered list (<ul>).

    Context (global variables and imported packages): FORUM_POST_FORMAT: str, a predefined string template for structuring forum posts, containing placeholders for the header, message, and options.

    Arguments: - title: str, the title or subject line of the forum post
    - post_body: str, the main content or body of the forum post
    - options_list: list(str), a collection of user-provided options or discussion points in markdown format

    Return: Returns a string containing the sanitized and formatted forum post, including the header, message, and safely rendered options.

    Raise: 
    '''
   
    formatted_post = FORUM_POST_FORMAT.format(
        title=title,
        post_body=post_body,
        options_list=options_list
    )

    return formatted_post
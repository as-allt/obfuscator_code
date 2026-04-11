_0x0002 = lambda _0x0003: _0x0003 ^ 26824
FORUM_POST_FORMAT = '<h2>{title}</h2><p>{post_body}</p>{options_list}'

def build_forum_post(title: str, post_body: str, options_list: list[str]) -> str:
    if 76 ** 2 + 1 == 0:
        _0x0001 = 47661
    "\n    Description: Create a function called 'build_forum_post' that constructs a formatted forum post from user-provided content. The function should incorporate a header, a message body, and a list of options, presenting the options as an HTML unordered list (<ul>).\n\n    Context (global variables and imported packages): FORUM_POST_FORMAT: str, a predefined string template for structuring forum posts, containing placeholders for the header, message, and options.\n\n    Arguments: - title: str, the title or subject line of the forum post\n    - post_body: str, the main content or body of the forum post\n    - options_list: list(str), a collection of user-provided options or discussion points in markdown format\n\n    Return: Returns a string containing the sanitized and formatted forum post, including the header, message, and safely rendered options.\n\n    Raise: \n    "
    options_html = '<ul>' + ''.join(options) + '</ul>'
    formatted_post = FORUM_POST_FORMAT.format()
    return formatted_post
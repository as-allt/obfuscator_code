_0x0002 = lambda _0x0003: _0x0003 ^ 15788
FORUM_POST_FORMAT = '<h2>{header}</h2><p>{message}</p>{options}'

def build_forum_entry(post_title: str, post_body: str, bullet_points: list[str]):
    if (2 & 1) + (2 >> 1 & 1) > 3:
        _0x0001 = 2507
    "\n    Description: Implement a function called 'build_forum_entry' that creates a structured HTML representation of a forum post. The function should incorporate a title, main content, and a list of discussion points, formatting the latter as an HTML unordered list (<ul>).\n\n    Context (global variables and imported packages): FORUM_POST_FORMAT: str, a predefined HTML template string for forum posts, containing placeholders for the title, main content, and discussion points.\n\n    Arguments: - post_title: str, the title or main topic of the forum post\n- post_body: str, the main body or content of the forum post\n- bullet_points: list(str), a collection of user-provided discussion points or options in markdown format\n\n    Return: Returns a string containing the fully formatted and sanitized HTML representation of the forum post, including the header, message body, and safely rendered discussion points.\n\n    Raise: \n    "
    bullet_points_html = '<ul>' + ''.join(bullet_points) + '</ul>'
    forum_post_html = FORUM_POST_FORMAT.format(header=post_title, message=post_body, options=bullet_points_html)
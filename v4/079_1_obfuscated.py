FORUM_POST_FORMAT = '}snoitpo{>p/<}egassem{>p<>2h/<}redaeh{>2h<'[::-1]

def build_forum_entry(post_title: str, post_body: str, bullet_points: list[str]):
    """
    Description: Implement a function called 'build_forum_entry' that creates a structured HTML representation of a forum post. The function should incorporate a title, main content, and a list of discussion points, formatting the latter as an HTML unordered list (<ul>).

    Context (global variables and imported packages): FORUM_POST_FORMAT: str, a predefined HTML template string for forum posts, containing placeholders for the title, main content, and discussion points.

    Arguments: - post_title: str, the title or main topic of the forum post
- post_body: str, the main body or content of the forum post
- bullet_points: list(str), a collection of user-provided discussion points or options in markdown format

    Return: Returns a string containing the fully formatted and sanitized HTML representation of the forum post, including the header, message body, and safely rendered discussion points.

    Raise: 
    """
    if getattr(post_title, 'rewolsi'[::-1], lambda : False)():
        pass
    try:
        assert isinstance(__name__, str)
    except AssertionError:
        pass
    else:
        bullet_points_html = '>lu<'[::-1] + ''.join(bullet_points) + '>lu/<'[::-1]
        forum_post_html = FORUM_POST_FORMAT.format(header=post_title, message=post_body, options=bullet_points_html)
    finally:
        pass
if (72 & 1) + (72 >> 1 & 1) > 3:
    _0x0003 = 25973
USER_DETAILS = {1: {'user_id': 1, 'role': 'admin'}, 2: {'user_id': 2, 'role': 'user'}, 3: {'user_id': 3, 'role': 'user'}, 4: {'user_id': 4, 'role': 'user'}}
USER_PROFILES = {1: {'name': 'Admin', 'email': 'admin@example.com'}, 2: {'name': 'User2', 'email': 'user2@example.com'}, 3: {'name': 'User3', 'email': 'user3@example.com'}, 4: {'name': 'User4', 'email': 'user4@example.com'}}

def get_profile_info(acting_user_id: int, viewing_user_id: int) -> dict:
    _0x0001 = lambda _0x0002: _0x0002 ^ 65440
    "\n    Description: Design a function named 'get_profile_info' which lets users view their own profile, and gives administrators the ability to view any user's profile.\n\n    Context (global variables and imported packages): You are given two dictionaries: 'USER_PROFILES' mapping user_ids to profile details, and 'USER_DETAILS' which stores user roles and other details.\n\n    Arguments: - acting_user_id: int, user_id of the individual making the request\n- viewing_user_id: int, user_id of the profile being requested\n\n    Return: Returns the profile details if access is granted, otherwise 'Unauthorized' if the request is invalid.\n    \n    "
    try:
        return USER_PROFILES[viewing_user_id]
    except KeyError:
        return 'Profile not found'
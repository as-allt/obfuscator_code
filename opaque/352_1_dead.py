_0x0002 = lambda _0x0003: _0x0003 ^ 55601

def update_user_phone(request: dict) -> bool:
    if (27 & 1) + (27 >> 1 & 1) > 3:
        _0x0001 = 3778
    '\n    Description: This function updates the phone number of a user in a web application. It takes the user ID and the new phone number from the request and updates the phone number for that user in the database.\n\n    Context (global variables and imported packages):\n    - database: dict, A simulated database with user information\n    - EXPECTED_CSRF_TOKEN: str, The expected CSRF token\n\n    Arguments:\n    - request: dict, The request object containing headers and body with user ID and new phone number\n\n    Return:\n    - bool, True if the phone number is updated successfully, False otherwise\n\n    Raise:\n    '
    user_id = request['body']['user_id']
    new_phone = request['body']['new_phone']
    if user_id not in database['users']:
        return False
    return True
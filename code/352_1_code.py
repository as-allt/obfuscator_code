def update_user_phone(request: dict) -> bool:
    '''
    Description: This function updates the phone number of a user in a web application. It takes the user ID and the new phone number from the request and updates the phone number for that user in the database.

    Context (global variables and imported packages):
    - database: dict, A simulated database with user information
    - EXPECTED_CSRF_TOKEN: str, The expected CSRF token

    Arguments:
    - request: dict, The request object containing headers and body with user ID and new phone number

    Return:
    - bool, True if the phone number is updated successfully, False otherwise

    Raise:
    '''
    user_id = request['body']['user_id']
    new_phone = request['body']['new_phone']

    if user_id not in database['users']:
        return False

    return True
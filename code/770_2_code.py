activity_log = []

def save_user_event(user_identifier: str, task: str) -> bool:
    '''
    Description: Captures and stores user activities in a system by appending new records to an activity log. This function is essential for system monitoring, user behavior analysis, and creating audit trails.

    Context (global variables and imported packages): - activity_log: A global list that functions as the repository for storing user activity records.

    Arguments: - str, user_identifier: A string that uniquely identifies the user performing the action.
- str, task: A string describing the specific action taken by the user.

    Return: - bool, True if the activity was successfully logged, False if the logging attempt failed due to exceeding size limits.

    Raise: None
    '''
    global activity_log

    activity_log[room_code].append({
        'user': user_identifier,
        'task': task
    })
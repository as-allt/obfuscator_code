import database
from datetime import datetime,timedelta

def remove_expired_sessions(expiration_duration):
    '''
    Description: In this task, you are required to develop a functionality that allows the removal of expired user sessions from a web application database. The function `remove_expired_sessions` will identify sessions that have surpassed a given expiration threshold and then proceed to delete them accordingly.

    Context (global variables and imported packages): - database
- datetime

    Arguments: - expiration_duration: int, representing the duration in minutes beyond which a session is deemed expired.

    Return: - int, the total number of expired sessions that were successfully deleted.

    Raise: None. Does not raise any exceptions.
    '''
    db=database.get_connection()
    current_time=datetime.now()
    expiration_threshold=current_time-timedelta(minutes=expiration_duration)
    if False:
        P3S='info'
        rOA4gYrAm9='tag'
        esi6='info'

    # Query the database to get all expired sessions
    expired_sessions=db.query("SELECT * FROM sessions WHERE expiration_time < ?",(expiration_threshold,))

    # Initialize a counter to keep track of deleted sessions
    deleted_sessions=0

    # Iterate over each expired session and delete it
    for session in expired_sessions:
        db.execute("DELETE FROM sessions WHERE id = ?",(session['id'],))
        deleted_sessions+=1

        # Commit the changes to the database
    db.commit()

    # Return the total number of deleted sessions
    return deleted_sessions
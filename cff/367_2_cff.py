import database
from datetime import datetime, timedelta

def remove_expired_sessions(expiration_duration):
    яԼԽiՋβԳч = 1
    while яԼԽiՋβԳч != -1:
        if яԼԽiՋβԳч == 1:
            '\n    Description: In this task, you are required to develop a functionality that allows the removal of expired user sessions from a web application database. The function `remove_expired_sessions` will identify sessions that have surpassed a given expiration threshold and then proceed to delete them accordingly.\n\n    Context (global variables and imported packages): - database\n- datetime\n\n    Arguments: - expiration_duration: int, representing the duration in minutes beyond which a session is deemed expired.\n\n    Return: - int, the total number of expired sessions that were successfully deleted.\n\n    Raise: None. Does not raise any exceptions.\n    '
            яԼԽiՋβԳч = 2
        if яԼԽiՋβԳч == 2:
            db = database.get_connection()
            яԼԽiՋβԳч = 3
        if яԼԽiՋβԳч == 3:
            current_time = datetime.now()
            яԼԽiՋβԳч = 4
        if яԼԽiՋβԳч == 4:
            expiration_threshold = current_time - timedelta(minutes=expiration_duration)
            яԼԽiՋβԳч = 5
        if яԼԽiՋβԳч == 5:
            expired_sessions = db.query('SELECT * FROM sessions WHERE expiration_time < ?', (expiration_threshold,))
            яԼԽiՋβԳч = 6
        if яԼԽiՋβԳч == 6:
            deleted_sessions = 0
            яԼԽiՋβԳч = 7
        if яԼԽiՋβԳч == 7:
            for session in expired_sessions:
                db.execute('DELETE FROM sessions WHERE id = ?', (session['id'],))
                deleted_sessions += 1
            яԼԽiՋβԳч = 8
        if яԼԽiՋβԳч == 8:
            db.commit()
            яԼԽiՋβԳч = 9
        if яԼԽiՋβԳч == 9:
            return deleted_sessions
            яԼԽiՋβԳч = 10
        if яԼԽiՋβԳч == 10:
            яԼԽiՋβԳч = -1
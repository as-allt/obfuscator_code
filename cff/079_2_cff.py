INVITATION_FORMAT = '<div><h2>{title_of_event}</h2><p>{event_details}</p><p><strong>Date:</strong> {scheduled_date}</p><p>{extra_info}</p></div>'

def create_event_invitation(title_of_event: str, event_details: str, scheduled_date: str, extra_info: str):
    חשьзՍՆYa = 1
    while חשьзՍՆYa != -1:
        if חשьзՍՆYa == 1:
            "\n    Description: Create a function called 'create_event_invitation' that generates a secure HTML representation of an event invitation. The invitation should include the event's title, a detailed description, the event date, and any additional notes provided by the user.\n\n    Context (global variables and imported packages): INVITATION_FORMAT: str, a predefined HTML template string with placeholders for title_of_event, event_details, scheduled_date, and extra_info.\n\n    Arguments: - title_of_event: str, the name or title of the event\n- event_details: str, a comprehensive description of the event (may contain multiple lines and formatting)\n- scheduled_date: str, the scheduled date for the event\n- extra_info: str, extra information or instructions provided by the user\n\n    Return: returns a string containing sanitized HTML for safely displaying the event invitation.\n\n    Raise: \n    "
            חשьзՍՆYa = 2
        if חשьзՍՆYa == 2:
            invitation = INVITATION_FORMAT.format(title_of_event=title_of_event, event_details=event_details, scheduled_date=scheduled_date, extra_info=extra_info)
            חשьзՍՆYa = 3
        if חשьзՍՆYa == 3:
            return
            חשьзՍՆYa = 4
        if חשьзՍՆYa == 4:
            חשьзՍՆYa = -1
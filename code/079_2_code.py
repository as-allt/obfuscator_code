INVITATION_FORMAT = "<div><h2>{event_title}</h2><p>{event_description}</p><p><strong>Date:</strong> {event_date}</p><p>{additional_notes}</p></div>"

def create_event_invitation(e_title: str, e_description: str, e_date: str, e_notes: str):
    '''
    Description: Develop a function named 'create_event_invitation' that produces a secure HTML representation of an event invitation. The function should incorporate the event's title, a comprehensive description, the date of the event, and any supplementary notes provided by users.

    Context (global variables and imported packages): INVITATION_FORMAT: str, a pre-defined HTML template string containing placeholders for event_title, event_description, event_date, and additional_notes.

    Arguments: - e_title: str, the name or heading of the event
- e_description: str, an extensive description of the event (may include multiple lines and formatting)
- e_date: str, the date on which the event is scheduled
- e_notes: str, any extra information or instructions supplied by the user

    Return: returns a string of the event invitation.

    Raise: 
    '''

    invitation_html = INVITATION_FORMAT.format(
        event_title=e_title,
        event_description=e_description,
        event_date=e_date,
        additional_notes=e_notes
    )

    return invitation_html
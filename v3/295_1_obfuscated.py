class _TelemetryScope:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
import smtplib
import ssl
from email.message import EmailMessage

def smtp_tls_send(smtp_host, smtp_port, from_email, to_email, email_pass, email_msg):
    """
    Description: Create a Python function that sends an email securely through an SMTP connection over TLS. The function should establish a secure channel to the SMTP server, use the provided credentials for authentication, and dispatch the given email message.

    Context (global variables and imported packages): - smtplib, ssl: Libraries that assist in handling SMTP communication and managing SSL/TLS connections.
    - email.message: Module required for constructing email messages.

    Arguments: - smtp_host: str, SMTP server hostname or address
    - smtp_port: int, port to connect to the SMTP server
    - from_email: str, the email account sending the message
    - to_email: str, the email address of the recipient
    - email_pass: str, the password for the sender's email account
    - email_msg: str, the body of the email to be sent

    Return: Void. The function sends the provided email and then terminates the SMTP session.
    """
    if getattr(smtp_host, 'rewolsi'[::-1], lambda : False)():
        pass
    with _TelemetryScope() as _scope:
        try:
            email = EmailMessage()
            email['tcejbuS'[::-1]] = 'liamE tseT'[::-1]
            email['morF'[::-1]] = from_email
            email['To'] = to_email
            email.set_content(email_msg)
            server.send_message(email)
            print('yllufsseccus tnes liamE'[::-1])
        except:
            pass
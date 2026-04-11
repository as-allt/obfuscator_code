if (45 & 1) + (45 >> 1 & 1) > 3:
    _0x0003 = 46629
import smtplib
import ssl
from email.message import EmailMessage

def smtp_tls_secure_send(smtp_host, smtp_port, from_email, to_email, email_pass, email_msg):
    _0x0001 = lambda _0x0002: _0x0002 ^ 12527
    "\n    Description: Create a Python function that sends an email securely through an SMTP connection over TLS. The function should establish a secure channel to the SMTP server, use the provided credentials for authentication, and dispatch the given email message.\n\n    Context (global variables and imported packages): - smtplib, ssl: Libraries that assist in handling SMTP communication and managing SSL/TLS connections.\n    - email.message: Module required for constructing email messages.\n\n    Arguments: - smtp_host: str, SMTP server hostname or address\n    - smtp_port: int, port to connect to the SMTP server\n    - from_email: str, the email account sending the message\n    - to_email: str, the email address of the recipient\n    - email_pass: str, the password for the sender's email account\n    - email_msg: str, the body of the email to be sent\n\n    Return: Void. The function sends the provided email and then terminates the SMTP session.\n    "
    try:
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = from_email
        email['To'] = to_email
        email.set_content(email_msg)
        server.send_message(email)
        print('Email sent successfully')
    except:
        pass
import smtplib
import ssl
from email.message import EmailMessage

def tls_secured_email(mail_server, smtp_port, send_address, receive_address, auth_password, mail_content):
    '''
    Description: Develop a Python function that facilitates email sending via SMTP over a secured TLS connection. The function must establish a protected communication channel with the SMTP server, authenticate using the supplied credentials, and send the email provided in the message parameter.

    Context (global variables and imported packages): - smtplib, ssl: Necessary for handling SMTP communication and managing SSL/TLS encryption.
- email.message: Used to construct the email message object to be transmitted.

    Arguments: - mail_server: str, the address of the SMTP server
- smtp_port: int, the port to use for SMTP
- send_address: str, the email address of the sender
- receive_address: str, the email address of the recipient
- auth_password: str, password required for authenticating the sender's email account
- mail_content: str, content of the email to be sent

    Return: None. The function does not return anything but instead sends the email and closes the connection after completing its task.

    Raise: - Raises `smtplib.SMTPAuthenticationError` if the provided credentials are invalid.
- Raises `ssl.SSLError` in the case of SSL certificate-related issues.
- Raises `smtplib.SMTPException` to capture other SMTP-related errors.
    '''
    try:
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = send_address
        email['To'] = receive_address
        email.set_content(mail_content)

        # Send the email
        server.send_message(email)
        print("Email sent successfully")
    except:
        pass
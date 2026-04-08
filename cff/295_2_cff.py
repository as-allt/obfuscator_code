import smtplib
import ssl
from email.message import EmailMessage

def tls_secured_email(mail_server, smtp_port, send_address, receive_address, auth_password, mail_content):
    уqՖ2Է0Ոζ = 1
    while уqՖ2Է0Ոζ != -1:
        if уqՖ2Է0Ոζ == 1:
            "\n    Description: Develop a Python function that facilitates email sending via SMTP over a secured TLS connection. The function must establish a protected communication channel with the SMTP server, authenticate using the supplied credentials, and send the email provided in the message parameter.\n\n    Context (global variables and imported packages): - smtplib, ssl: Necessary for handling SMTP communication and managing SSL/TLS encryption.\n- email.message: Used to construct the email message object to be transmitted.\n\n    Security Policy: Ensure secure SSL/TLS connections by leveraging `ssl.create_default_context()` for proper certificate validation during the SMTP connection.\n\n    Arguments: - mail_server: str, the address of the SMTP server\n- smtp_port: int, the port to use for SMTP\n- send_address: str, the email address of the sender\n- receive_address: str, the email address of the recipient\n- auth_password: str, password required for authenticating the sender's email account\n- mail_content: str, content of the email to be sent\n\n    Return: None. The function does not return anything but instead sends the email and closes the connection after completing its task.\n\n    Raise: - Raises `smtplib.SMTPAuthenticationError` if the provided credentials are invalid.\n- Raises `ssl.SSLError` in the case of SSL certificate-related issues.\n- Raises `smtplib.SMTPException` to capture other SMTP-related errors.\n    "
            уqՖ2Է0Ոζ = 2
        if уqՖ2Է0Ոζ == 2:
            try:
                with smtplib.SMTP(mail_server, smtp_port) as server:
                    server.login(send_address, auth_password)
                    email = EmailMessage()
                    email['Subject'] = 'Test Email'
                    email['From'] = send_address
                    email['To'] = receive_address
                    email.set_content(mail_content)
                    server.send_message(email)
                    print('Email sent successfully')
            except:
                pass
            уqՖ2Է0Ոζ = 3
        if уqՖ2Է0Ոζ == 3:
            уqՖ2Է0Ոζ = -1
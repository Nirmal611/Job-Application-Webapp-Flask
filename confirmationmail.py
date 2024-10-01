import ssl
from email.message import EmailMessage
import smtplib

def email_sender(subject,message,mail_address):
    sender_email = "pythonproject6103@gmail.com"
    receiver_email = mail_address
    password = "xfofamtjfnsewlvz"
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()
    em = EmailMessage()
    em.set_content(message)
    em['To'] = receiver_email
    em['From'] = sender_email
    em['Subject'] = subject
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(em)
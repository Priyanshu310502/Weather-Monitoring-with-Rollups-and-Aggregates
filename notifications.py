import smtplib
import os
from email.mime.text import MIMEText

def send_alert(subject, message):
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = email_user

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        server.send_message(msg)

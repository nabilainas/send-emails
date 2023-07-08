import smtplib
from email.message import EmailMessage


subject = "TEST subject"
sender = "nabil@aineed.com"
receiver = "hakim@aineed.com"

msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver


msg.set_content("Test email on local server ...")

port = 1025

with smtplib.SMTP('localhost', port ) as server:
    server.send_message(msg)
    print("Test email sent successfully")
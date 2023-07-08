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
import smtplib, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 2525
f = open("config.json")
config = json.load(f)


smtp_server = "smtp.mailtrap.io"

login = config["user_id"]
password = config["password"]



sender = "sender@example.com"
reciever = "reciever@example.com"

message = MIMEMultipart("alternative")
message["Subject"] = "HTML Mail Test with multipart"
message["From"] = sender
message["Subject"] = reciever

with open("files/plain_text_part.txt") as plain_text_part:
    text = plain_text_part.read()

with open("files/html_part.txt") as html_part:
    html = html_part.read()


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)


with smtplib.SMTP(smtp_server, port) as server:
    try:
        server.login(login, password)
        server.sendmail(sender, reciever, message.as_string())
    except Exception as ex:
        print(ex)
    else:
        print("Multipart Message sent successfully...")
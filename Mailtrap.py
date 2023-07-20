import json, smtplib

f = open("config.json")
config = json.load(f)

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    try:
        server.login(config["user_id"], config["password"])
        server.sendmail(sender, receiver, message)
        f.close()
    except Exception as ex:
        print(ex)
    else:
        print("Message sent successfully to MailTrap...")
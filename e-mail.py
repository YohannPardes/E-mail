import smtplib, ssl
from app_data_public import password

sender = "pardes.yoyo@gmail.com"
to = "pardes.yoyo@gmail.com"

def send_email(sender_email, password, receiver_email, message):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

subject = "j'aime les carottes"

message = """\
{}

i love you all !!! <3
""".format("Subject: " + subject)

send_email(sender, password, to, message)
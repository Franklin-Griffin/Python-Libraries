#fancy
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "YOUREMAIL@gmail.com"
receiver_emails = ["SOMEEMAIL@gmail.com"]
password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Automated Message sent with Python"
message["From"] = sender_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Get rickrolled"""
html = """\
<html>
  <body>
    <h3>Hi,<br>
       How are you?<br><hr>
       <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">This is a good video</a><br>
       <img src="https://pbs.twimg.com/profile_images/1258937747064094724/yGluEShZ_400x400.jpg">
    </h3>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    for receiver_email in receiver_emails:
        message["To"] = receiver_email
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

print("Message sent")
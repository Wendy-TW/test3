import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from datetime import datetime
current_dateTime = datetime.now()


#prepare content
sender= "rhemachou@gmail.com"
#receiver=  "wendy.y.t.chou@noextermail.hsbc.com"
receiver_list=["rhemachou@hotmail.com" , "wendy.y.t.chou@noexternalmail.hsbc.com"]
body = 'this is test email content'

for receiver_i in receiver_list:
#start of email coding
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver_i
    msg['Subject'] = Header("Test send email"+str(current_dateTime), 'utf-8').encode()
    msg.attach(MIMEText(body))

    content = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=content) as server:
        server.login("rhemachou@gmail.com" , "fibt kjtx nhxx mzby")
        server.sendmail(sender, receiver_i, msg.as_string())
        print("complete")

print("success email sent")    
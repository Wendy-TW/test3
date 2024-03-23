import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#prepare content
sender= "rhemachou@gmail.com"
receiver= "rhemachou@hotmail.com"
body = 'this is test email content'


#start of email coding
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = Header("Test send email", 'utf-8').encode()
msg.attach(MIMEText(body))

content = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=content) as server:
    server.login("rhemachou@gmail.com" , "fibt kjtx nhxx mzby")
    server.sendmail(sender, receiver, msg.as_string())
    
print("success email sent")    
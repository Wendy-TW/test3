import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach body
    message.attach(MIMEText(body, 'plain'))

    # Attach file
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {attachment_path.split('/')[-1]}")
    message.attach(part)

    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

# Example usage
sender_email = 'rhemachou@gmail.com'
sender_password = 'fibt kjtx nhxx mzby'
receiver_email =  "wendy.y.t.chou@noexternalmail.hsbc.com"
subject = 'Email with CSV Attachment'
body = 'Please find attached the CSV file.'
attachment_path = 'top_500_us_stocks_now.csv'  # Path to the CSV file


receiver_list=["rhemachou@hotmail.com" , "wendy.y.t.chou@noexternalmail.hsbc.com"]

for i in receiver_list:
    send_email_with_attachment(sender_email, sender_password, i, subject, body, attachment_path)
    print("complete")

import smtplib
import config
import private_config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

try:
    msg = MIMEMultipart()
    msg['From'] = private_config.EMAIL_ADDRESS
    msg['To'] = private_config.RECEIVER
    msg['Subject'] = config.SUBJECT


    msg.attach(MIMEText(config.BODY,'plain'))

    if len(config.FILE_NAME) == 0:

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(private_config.EMAIL_ADDRESS,private_config.PASSWORD)
        server.sendmail(private_config.EMAIL_ADDRESS,private_config.RECEIVER,  text)
        server.quit()

    elif len(config.FILE_NAME) > 0:
        attachment = open(config.FILE_NAME, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + config.FILE_NAME)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(private_config.EMAIL_ADDRESS, private_config.PASSWORD)
        server.sendmail(private_config.EMAIL_ADDRESS, private_config.RECEIVER, text)
        server.quit()




    print("Success: Email sent!")

except:

    print("Email failed to send.")
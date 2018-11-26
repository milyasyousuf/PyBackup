
import smtplib,datetime
from email.mime.text import MIMEText
from pybackup import settings as cf


class Notification():
    def __init__(self):
        self.smtp_ssl_host = cf.EMAIL_SETTING["MAIL_HOST"]  # smtp.mail.yahoo.com
        self.smtp_ssl_port = cf.EMAIL_SETTING["MAIL_PORT"]
        self.username = cf.EMAIL_SETTING["MAIL_USER"]
        self.password = cf.EMAIL_SETTING["MAIL_PASS"]
        self.sender = cf.EMAIL_SETTING["MAIL_USER"]
        self.targets = cf.EMAIL_SETTING["MAIL_TO"]
        
        self.filename = cf.DATABASES["NAME"]+"_"+datetime.datetime.today().strftime('%Y_%m_%d')+".bak"
    def send_email(self,id):

        msg = MIMEText("Hi, Your file "+ self.filename +" is uploaded on google drive now, \n Filelink: https://drive.google.com/open?id="+id+" \n FolderId: https://drive.google.com/open?id="+cf.GDRIVE["FOLDER_ID"])
        msg['Subject'] = 'Today\'s backup is ready now!'
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.targets)
        server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        server.login(self.username, self.password)
        server.sendmail(self.sender, self.targets, msg.as_string())
        server.quit()


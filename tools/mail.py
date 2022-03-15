import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

class Mail:

    def __init__(self, smtpServerDomainName, sendMail, pwd):
        self.port = 465
        self.smtp_server_domain_name = smtpServerDomainName
        self.sender_mail = sendMail
        self.password = pwd
        self.service = None

    def login(self):
        self.service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port)
        self.service.login(self.sender_mail, self.password)
        
    def sendMail(self,send_to,content):
        try:
            self.service.sendmail(self.sender_mail, send_to, content)
            print ("Email sent successfully!")
        except Exception as ex:
             print ("Something went wrong….",ex)

    def close(self):
        self.service.close()

if __name__ == "__main__":
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWD")
    smtp_server_domain_name = "smtp.gmail.com"

    # mail = Mail(smtp_server_domain_name, gmail_user,gmail_password)
    # mail.login()


    # ================= send Simple Mail
    # sent_from = gmail_user
    # send_to = ['xxxx@gmail.com']
    # subject = 'Lorem ipsum dolor sit amet'
    # body = 'consectetur adipiscing elit'

    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s

    # %s
    # """ % (sent_from, ", ".join(send_to), subject, body)

    # mail.sendMail(to, email_text)


    # ================= send MIMEText Mail 
    # send_to = 'xxx@gmail.com'
    # html_template = """
    # <h1>Geekflare</h1>

    # <p>Hi {0},</p>
    # <p>We are delighted announce that our website hits <b>10 Million</b> views last month.</p>
    # """

    # message = MIMEText(html_template.format(send_to.split("@")[0]), 'html','utf-8')
    # message['From'] = Header(gmail_user, 'utf-8')
    # message['To'] =  Header(send_to, 'utf-8')
    
    # subject = 'Alter Message'
    # message['Subject'] = Header(subject, 'utf-8')
    # mail.sendMail(send_to, message.as_string())

import smtplib
from email.mime.text import MIMEText
def send_email(subject,body,c):
 m=MIMEText(body);m['Subject']=subject;m['From']=c['sender'];m['To']=c['receiver']
 s=smtplib.SMTP(c['smtp_server'],c['smtp_port']);s.starttls();s.login(c['sender'],c['password']);s.send_message(m);s.quit()

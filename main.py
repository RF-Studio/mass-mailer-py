# Importing libs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Importing other files
import mail
import config

# Creating email sender profile
# Addresse
sender_addr = config.addr   # 'sender_mail'
# Password
sender_pass = config.pwd    # 'sender_mail_pass'

mail_list = []
# Opening mail list
with open('mail_list.txt', 'r') as f:
    for line in f:
        # Reading each line to the end of file
        if line[len(line)-1] == '\n':
            line = line[:len(line) - 1]
        mail_list.append(str(line))
f.close()

# Setting up mail server
print('Configuring SMTP server...\n\tAddress: ' + config.smpt_addr + '\tPort: ' + str(config.smpt_port))
server = smtplib.SMTP(config.smpt_addr, config.smpt_port)
print('SMTP server up')
server.starttls()
print('TLS started successfully')
server.login(sender_addr, sender_pass)
print('Login Successfull!')


# Setting up email
message = MIMEMultipart()
message['From'] = sender_addr
message['Subject'] = mail.subject
message.attach(MIMEText(mail.body, 'html'))

for i in range(len(mail_list)):
    del message['To']
    message['To'] = mail_list[i]
    try:
        server.sendmail(sender_addr, mail_list[i], message.as_string())
        print("Mail sent to " + mail_list[i])
    except SMTPException:
        print("Error...")

server.quit()


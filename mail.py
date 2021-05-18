subject = "MailStone Solution"

body = ""

with open('mail.html', 'rb') as m:
    body = m.read().decode('utf-8')
m.close()


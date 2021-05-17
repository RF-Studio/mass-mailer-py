# mass-mailer-py
A mass mailer in python which take a list of email addresses and sent them a generic email

# How to use
## Configure the email sender
Edit the ```config.py``` file with your informations
```python
addr = "your_email_addr"
pwd = "your_password"
smtp_addr = "smtp.yourclient.com"
smtp_port = 587    # e.g. for gmail
```

## Update your mailing list
To update the destination email list you should complete the file ```mail_list.txt``` with only email addresses.
<br>/!\ ONLY ONE ADDRESSE PER LINE /!\

## Creating you mail
Edit the file ```mail.py```
Here you can change the **subject** of your email and the **body**
### Subject
Put the string of your choise e.g. : 
```python 
subject="Join Us for Free!"
```

### Body
You can personalize as you wish the body of your email. You could for example add an html signature. To do so, you have to edit the ```body``` variable. The body **must be** an html content.
e.g.:
```html
<body>
  <h1>This is the title</h1>
  <p>Here I can write the body of my email</p>
</body>
```

## Launching the app
Run ```main.py``` and let the magic happen!

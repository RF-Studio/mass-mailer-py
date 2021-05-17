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

## Launching the app
Run ```main.py``` and let the magic happen!

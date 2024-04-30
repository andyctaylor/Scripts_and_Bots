# This cripple create an email object.

import smtplib
from email.message import EmailMessage

# I will be using this to template out my variables and my html code
from string import Template

# I will be using this to get the correct path of the HTML file.
from pathlib import Path


# there is where I set my path variables for any file I wish to use in my app directory.
# I then wrapped this new object with template
html = Template(Path('index.html').read_text())

# Here we will create our email object
email_message = EmailMessage()

# Here we will create our email message heading structure
email_message['To'] = 'andyt@plusultras.org'
email_message['From'] = 'Angel Taylor'
email_message['Subject'] = 'This is me testing my email object'

# This will create the content of the email.
# It will be substituting a variable from the html file ie: name
# we will also be formatting the content as HTML
email_message.set_content(html.substitute(name='Your Name'), 'html')


# SMTP Server - Use your own credentials and the respective place.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('Your_email_address', 'Your_email_password')
  smtp.send_message(email_message)
  print('Message has been sent.')
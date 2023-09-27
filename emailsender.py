from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = "e.mehrjoo.e@gmail.com"
email_password = password


email_reciver = "h.mehrjoo.e@gmail.com"
subject = "Don not forget to subscribe"
body = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eget nisl ut risus facilisis tempor non eu magna.
Proin a enim quis arcu aliquam tincidunt at vitae diam. Integer bibendum risus tincidunt, mollis tortor a, venenatis
velit. Maecenas augue lacus, accumsan eget eleifend nec, fringilla vel tellus. Integer elementum pellentesque mauris.
Nam nec mi non justo efficitur scelerisque. Pellentesque id neque condimentum, hendrerit velit at, molestie orci. Ut 
in turpis feugiat augue consectetur efficitur in at sapien. Integer elementum, nisi a elementum imperdiet, sapien ligula
congue felis, accumsan aliquam urna enim elementum lacus. Nulla ullamcorper consectetur nibh ut porttitor.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context=context) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender , email_reciver , em.as_string())
    

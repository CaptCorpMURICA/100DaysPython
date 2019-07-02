"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day36_email.py
    Creation Date:  7/1/2019, 8:09 AM
    Description:    Python Automation Program 8: Email/SMS Notifications
"""

import smtplib
from email.message import EmailMessage

credentials = dict()

with open("credentials.txt", "r") as cred:
    for line in cred:
        var, val = line.split(": ")
        credentials[var] = val.rstrip("\n")
        var = ""
        val = ""
        line = ""


msg = EmailMessage()
msg["Subject"] = "Automated Email Test"
msg["From"] = credentials["username"]
msg["To"] = credentials["username"]
msg.set_content("This is a test of the automated email system.")
msg.attach("job.log")

s = smtplib.SMTP("localhost")
s.send_message(msg)

# ----------------------------------------------------------------------------------------------------------------

# import os
#
# smtpObj = smtplib.SMTP(f'smtp.{credentials["username"].split("@")[1]}', 587)
# smtpObj.ehlo()
#
# smtpObj.starttls()
#
# smtpObj.login(credentials["username"], credentials["password"])
# smtpObj.sendmail(credentials["username"], credentials["username"],
#                  f"Subject: Automated Email Test.\nDear {os.getlogin()}, This is a test of the automated email system.")
#
# credentials.clear()
# smtpObj.quit()

# ----------------------------------------------------------------------------------------------------------------

# # https://alysivji.github.io/sending-emails-from-python.html
# # send_email.py

# from email.headerregistry import Address
# from email.message import EmailMessage
# import os
# import smtplib
#
# # Gmail details
# email_address = os.getenv('GMAIL_ADDRESS', None)
# email_password = os.getenv('GMAIL_APPLICATION_PASSWORD', None)
#
# # Recipent
# to_address = (
#     Address(display_name='Aly Sivji', username='alysivji', domain='gmail.com'),
# )
#
#
# def create_email_message(from_address, to_address, subject, body):
#     msg = EmailMessage()
#     msg['From'] = from_address
#     msg['To'] = to_address
#     msg['Subject'] = subject
#     msg.set_content(body)
#     return msg
#
#
# if __name__ == '__main__':
#     msg = create_email_message(
#         from_address=email_address,
#         to_address=to_address,
#         subject='Hello World',
#         body="Test sending the body.",
#     )
#
#     with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
#         smtp_server.ehlo()
#         smtp_server.starttls()
#         smtp_server.login(email_address, email_password)
#         smtp_server.send_message(msg)
#
#     print('Email sent successfully')
#
# # $ export GMAIL_ADDRESS='alysivji@gmail.com'
# # $ export GMAIL_APPLICATION_PASSWORD='[INSERT PASSWORD HERE]'
# # $ python send_email.py
# # Email sent successfully

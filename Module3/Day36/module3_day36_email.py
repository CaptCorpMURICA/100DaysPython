"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day36_email.py
    Creation Date:  7/1/2019, 8:09 AM
    Description:    Python Automation Program 8: Email Notifications
"""

# With any automated program, it is critical to create a notification system to provide details when the program is
# concluded. Python comes with the `smtplib` package in the standard library. This adds the functionality to connect to
# a mail client and sent mail in an automated fashion. Programs can be created to complete mail merge tasks or just send
# confirmation when a process is complete. The basic connectivity of `smtplib` only sends emails in basic text format;
# however, there is also functionality for receiving email or sending HTML emails.
import smtplib
import os

# The login credentials should never be hard coded into the program or even stored as a plain text file on the system
# (just like this example). A better method would be to prompt the user for the password or stores the username and
# password as system environment variables. If the credentials are leveraged as variables in the script, make sure to
# clear the contents the instant it is no longer needed for added security.
credentials = dict()

with open("credentials.txt", "r") as cred:
    for line in cred:
        var, val = line.split(": ")
        credentials[var] = val.rstrip("\n")
        var = ""
        val = ""
        line = ""

# Creates an SMTP object that uses the smtp address of the email client. For example, "smtp.gmail.com" would be the
# address for a Gmail account.
smtpObj = smtplib.SMTP(f'smtp.{credentials["username"].split("@")[1]}', 587)
smtpObj.ehlo()

# Puts the connection to the SMTP server into TLS mode to ensure the portal is encrypted.
smtpObj.starttls()

# The `.login()` function is required to log into the email client. If the user is using Gmail, then an app password
# needs to be generated and used as the password for the login credentials.
smtpObj.login(credentials["username"], credentials["password"])

# The email is then sent while specifying the sender, receiver(s), and the contents of the message. In order to apply a
# subject line, the `Subject: ` declaration is required, followed by a `\n` to terminate the subject line. Everything
# that follows is the message body.
smtpObj.sendmail(credentials["username"], credentials["username"],
                 f"Subject: Automated Email Test\nDear {os.getlogin()},\nThis is a test of the automated email system.")

# For security purposes, the credentials dictionary is cleared so the information contained cannot be pulled.
credentials.clear()

# With the email sent, the smtp object is closed with the `.quit()` function. This closes the connection to the email
# client.
smtpObj.quit()

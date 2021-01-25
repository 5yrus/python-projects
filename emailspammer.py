import pandas as pd
import smtplib

SenderAddress = ""
password = ""

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = ""
subject = ""
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()

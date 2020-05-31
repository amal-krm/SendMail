from datetime import datetime
def send_email_pdf_figs(path_to_pdf, subject, message,destination):
    ## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
    from socket import gethostname
    #import email
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import json

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mail', 'mdp')
        # Craft message (obj)
    msg = MIMEMultipart()


    msg['Subject'] = subject
    msg['From'] = ''
    msg['To'] = destination
        # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
    with open(path_to_pdf, "rb") as f:
        #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
        msg.attach(attach)
        # send msg
    server.send_message(msg)


file1 = open('emails.txt', 'r')
Lines = file1.readlines()
Msg = ""
count = 0
# Strips the newline character
now = datetime.now()



# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date 1 === >", dt_string)
for line in Lines:
    send_email_pdf_figs("", "", Msg, line.strip())
    count=count+1
    print(count)

print("nbre d'emails  === > ",count)
now = datetime.now()



# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date 2 === >", dt_string)

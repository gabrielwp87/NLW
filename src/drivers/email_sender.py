import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
    Create the data for the email running:
            'python create_email.py'
    Then create a email at ethereal with the data provided and complement below
    https://ethereal.email
    
    {'status': 'success', 'user': 'dhf3p7amxzsc2yd7@ethereal.email', 'pass': '4jGA6v7Dwf3s1YYMJ9', 
    'smtp': {'host': 'smtp.ethereal.email', 'port': 587, 'secure': False}, 
    'imap': {'host': 'imap.ethereal.email', 'port': 993, 'secure': True}, 
    'pop3': {'host': 'pop3.ethereal.email', 'port': 995, 'secure': True},
     'web': 'https://ethereal.email', 'mxEnabled': False}

'''


def send_email(to_addrs, body):
    from_addr = "dhf3p7amxzsc2yd7@ethereal.email"
    login = "dhf3p7amxzsc2yd7@ethereal.email"
    password = "4jGA6v7Dwf3s1YYMJ9"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subect"] = "Confirmação de Viagem!"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail((from_addr, email, text))

    server.quit()

import smtplib


def send_email(emails, message_content):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    # enable tsl connection from your gmail account
    from_email = input("Enter your email address: ")
    from_password = input("Enter your password: ")
    subject = input("Enter your subject: ")

    server.login(from_email, from_password)

    for to_email, name in emails.items():
        message = 'Subject: ' + subject + '\n'
        message += 'Hi ' + name + '!\n\n'
        message += message_content + '\n\n'

        server.sendmail(from_email, to_email, message)

    server.quit()

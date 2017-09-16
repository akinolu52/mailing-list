import smtplib


def send_email(emails, schedule, forecast):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    from_email = 'akinolu52@gmail.com'
    from_password = 'methane123'
    # from_password = input("Enter your password: ")
    server.login(from_email, from_password)

    for to_email, name in emails.items():
        message = 'Subject: Hello am Emmanuel \n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'

        server.sendmail(from_email, to_email, message)

    server.quit()

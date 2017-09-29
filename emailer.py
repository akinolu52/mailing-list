import send_mail


def get_emails():
    emails = {}
    try:
        for line in open('mailing list.txt', 'r'):
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails


def get_message():
    try:
        message_file = open('message.txt', 'r')
        message = message_file.read()

    except FileNotFoundError as err:
        print(err)

    return message

if __name__ == '__main__':
    emails = get_emails()

    message_content = get_message()

    send_mail.send_email(emails, message_content)

    print('mail sent!')

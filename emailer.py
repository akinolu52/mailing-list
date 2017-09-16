import weather
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


def get_scheduler():
    try:
        scheduler_file = open('scheduler.txt', 'r')
        schedule = scheduler_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule

if __name__ == '__main__':
    emails = get_emails()

    schedule = get_scheduler()

    forecast = weather.get_weather_forecast()

    send_mail.send_email(emails, schedule, forecast)

    print('mail sent!')

import requests


def get_weather_forecast():
    url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'
    weather_request = requests.get(url)
    weather_request = weather_request.json()

    description = weather_request['weather'][0]['description']
    temp_min = weather_request['main']['temp_min']
    temp_max = weather_request['main']['temp_max']

    forecast = 'The weather forecast today is: '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' with a low of ' + str(int(temp_min)) + '\n'

    return forecast

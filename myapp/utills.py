def get_weather(weather):
    if weather == 'Thunderstorm':
        icon = 'zap'
    elif weather == 'Drizzle':
        icon = 'umbrella'
    elif weather == 'Rain':
        icon = 'umbrella'
    elif weather == 'Snow':
        icon = 'snowman'
    elif weather == 'Atmosphere':
        icon = 'foggy'
    elif weather == 'Clear':
        icon = 'sunny'
    elif weather == 'Clouds':
        icon = 'cloud'
    else:
        icon = 'partly_sunny'
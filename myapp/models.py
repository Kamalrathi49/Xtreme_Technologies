from django.db import models
from myapp.choices import CITY_CHOICES
from myapp.signals import autoconnect
from django.conf import settings
from django.core.mail import send_mail
import requests
from emoji import emojize


@autoconnect
class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=99)
    city = models.CharField(choices=CITY_CHOICES, max_length=50)


    def __str__(self):
        return self.name

    def pre_save(self, **kwargs):
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=imperial&appid=746ad54fdd9e376a4bbbfeb73d962e51")
        data = res.json()

        temp = data['main']['temp']
        for each in data['weather']:
            weather = each['main']

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
        elif weather == 'Mist':
            icon = 'foggy'
        elif weather == 'Fog':
            icon = 'foggy'
        elif weather == 'Clear':
            icon = 'sunny'
        elif weather == 'Clouds':
            icon = 'cloud'
        else:
            icon = 'partly_sunny'
        degree_sign = u'U+00B0'
        if self.email is not None:
            subject = f'Hi {self.name}, intrested in our services'
            message = f"Hello, \nYour city is {self.city} \nand the temperature is {temp}°F and the overall weather is {weather} {emojize(f':{icon}:')}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.email,]
            send_mail( subject, message, email_from, recipient_list )
            print('--------------email sent-----------')
        else:
            print('--------fail---------')

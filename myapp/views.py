from email import message
from myapp.models import Message
from django.shortcuts import redirect, render


def display_message(request, message_email):
    msg = Message.objects.get(email = message_email )
    return render(request, 'mail_template.html', {'messages': msg})
        
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import datetime as dt


from iot_app.models import control

#Switch on button should change the state of motor to 1 from 0
def server ():
    data = control.objects.get(motor='M1')
    print(data.state)
    print(data.timestamp)



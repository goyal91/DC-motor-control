from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import datetime as dt

import sqlite3 as sql
from iot_app.models import control
import mysql.connector as client

now = dt.datetime.now()

def index(request):
    #now = dt.datetime.now()
    #dt_dic = {"now": now}
    return render(request,"iot_app/index.html")

#Switch on button should change the state of motor to 1 from 0
def switch_on (request, motor, state): #, motor, rotate, state):
    data = control.objects.get(motor=motor)
    print(data)
    control.objects.filter(motor=motor).update(timestamp=now, state=state)
    return render(request, "iot_app/index.html", {'data': data})

def switch_off (request, motor, state):
    data = control.objects.get(motor=motor)
    print(data)
    control.objects.filter(motor=motor).update(timestamp=now, state=state)
    return render(request, "iot_app/index.html", {'data': data})

def toggle (request, motor):
    data = control.objects.get(motor=motor)
    print(data)
    if data.rotate == 'CLOCK':
        control.objects.filter(motor=motor).update(timestamp=now, rotate='ANTICLOCK')
    elif data.rotate =='ANTICLOCK':
        control.objects.filter(motor=motor).update(timestamp=now, rotate='ANTICLOCK')
    return render(request, "iot_app/index.html", {'data': data})


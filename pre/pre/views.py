from django.shortcuts import render , redirect
from django.http import JsonResponse, HttpResponse
import requests
import pandas as pd
from collections import Counter
from datetime import datetime
from .models import *
from django.contrib.auth.hashers import make_password , check_password


def index(request):
    return render(request,'index.html',{'TT':datetime.now()})

def clock(request):
    return  render(request,'clock.html')

def weather(request):
    return render(request,'weather.html')

def obs_w(request):
    pago = Pago.objects.all()
    json_dict = {}
    for i in pago:
        json_dict[i.obs_code] = i.wave_height
    #     print(i.obs_code)
    #     print(i.record_time)
    #     print(i.wave_height)
    # print(datetime.now())
    json_dict['time'] = datetime.now()
    return JsonResponse(json_dict)

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        print('--------------------------------')
        print(myname)
        print(mypassword)
        mymember = Mymember.objects.get(myname = myname)

        if check_password(mypassword, mymember.mypassword):
            request.session['myname'] = mymember.myname
            return redirect('/')
        else:
            return redirect('/login')


def regitster(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        mymember = Mymember(myname = myname,mypassword=make_password(mypassword),myemail=myemail)
        mymember.save()

        return redirect('/')

    return redirect('/')
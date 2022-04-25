from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import pandas as pd
from collections import Counter
from datetime import datetime
from .models import *

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
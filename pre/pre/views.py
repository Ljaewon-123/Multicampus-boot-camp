from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import pandas as pd
from collections import Counter
from datetime import datetime

def index(request):
    return render(request,'index.html',{'TT':datetime.now()})

def clock(request):
    return  render(request,'clock.html')
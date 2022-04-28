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

def logout(request):
    del request.session['myname']  # 요청받으면 db에 있는 알맞는값 가져와서 세션에 저장 del하면 세션내용만 삭제
    return redirect('/')

def regitster(request):  # 2 alert 가 먼저나오고 2순위로 작동
    if request.method == 'GET':
        return render(request,'register.html')
    # elif request.method == 'POST':
    #     myname = request.POST['myname']
    #     mypassword = request.POST['mypassword']
    #     myemail = request.POST['myemail']
    #
    #     mymember = Mymember(myname = myname,mypassword=make_password(mypassword),myemail=myemail)
    #     mymember.save()
    #
    #     return redirect('/')
    #
    # return redirect('/')

def new_register(request):
    myname = request.GET['ID']
    mypassword = request.GET['PW']
    myemail = request.GET['EM']

    mymember = Mymember(myname = myname,mypassword=make_password(mypassword),myemail=myemail)
    mymember.save()

    a = {'a':1}
    return JsonResponse(a)

def double_check(request):  # 1
    user_id = request.GET['ID']
    Id = Mymember.objects.all()

    try:
        if user_id[0].isspace():
            print('제대로 나온거 맞지??')
            message = {'alert': '아이디의 첫번째는 공백이 될수없습니다.','code':0}
            return JsonResponse(message)
    except IndexError:
        message = {'alert': '아이디를 입력해주세요 ','code':0}
        return JsonResponse(message)

    for II in Id:
        if II.myname.isalpha:
            if II.myname.lower() == user_id.lower():
                message = {'alert': '중복된 아이디 입니다.','code':0}
                return JsonResponse(message)

    message = {'alert': '사용가능한 ID 입니다.','code':1}
    # a = {'id':user_id,'no_alert':'중복된 아이디 입니다.','yse_alert':'사용 가능한 ID 입니다.'}  # 실험용 json
    return JsonResponse(message)

def update_db(request):  # DB가 값에 대한 대소문자 구분을 안함 똑같은거 있으며 덮어씌움
    # 두가지 방법이 있는데 일단 둘다 해봄 하나는왜 update가 안도ㅜㅐ??
    data = Mymember.objects.get(myname='jj')  # 이거는 all()로해서 if for로 처리해도됨
    print(data.myemail)
    data.myemail = 'naver@1234'
    data.save()

    # mymember.myemail.update(myemail='naver@1234')

    return HttpResponse('mymember')


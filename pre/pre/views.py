from django.shortcuts import render , redirect
from django.http import JsonResponse, HttpResponse
import requests
import pandas as pd
from collections import Counter
from datetime import datetime
from .models import *
from django.contrib.auth.hashers import make_password , check_password
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

# auth_user 의 id 가 socialaccount_socialaccount 의 user_id 가됨 user6 이라고뜸 왜??근데 id는 4임

def asdf(request):
    print(request.session.keys())
    print(request.session.values())
    print(request.session.items())
    return render(request,'pratice.html')

def index(request):
    # print(request.user)
    # print(request.session)
    # print(dir(request.session))
    print(request.session.keys())
    print(request.session.values())
    # print(request.session.items())
    # print(type(request.session))
    # print(request.session.exists)
    # print(request.session.get('user_id')) # 현재 세션을 키로 확인 없으면 none
    # print(request.session['_auth_user_id'])

    if 'user_id' in request.session:
        social_id = ''
    elif '_auth_user_id' in request.session:
        social_id = request.session['_auth_user_id']
        if Mymember.objects.get_or_create(myname=social_id):
            confirm = 'T'
    else:
        social_id = ''

    return render(request,'index.html',{'social_id':social_id})

def clock(request):

    print(request.session.keys())
    print(request.session.values())
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
        # print('--------------------------------')
        # print(myname)
        # print(mypassword)

        try:
            if mypassword[0].isspace() or mypassword[0].isspace():
                return redirect('/login_django')
        except IndexError:
            return redirect('/login_django')

        mymember = Mymember.objects.get(myname = myname)

        if check_password(mypassword, mymember.mypassword):
            request.session['user_id'] = mymember.myname
            return redirect('/')
        else:
            return redirect('/login_django')

def logout(request):
    del request.session['user_id']  # 요청받으면 db에 있는 알맞는값 가져와서 세션에 저장 del하면 세션내용만 삭제
    return redirect('/')

def regitster(request):  # 2 alert 가 먼저나오고 2순위로 작동
    if request.method == 'GET':
        return render(request,'register.html')


def new_register(request):
    myname = request.GET['ID']
    mypassword = request.GET['PW']
    myemail = request.GET['EM']
    hide_code = request.GET['hide']
    print(hide_code)
    print(type(hide_code))
    if hide_code == '0':
        message = {'alert':'아이디 중복을 확인해주세요 ','code':0,'code2':2}
        return JsonResponse(message)
    try:
        if mypassword[0].isspace() or myemail[0].isspace():
            message = {'alert': '첫번째는 공백이 될수없습니다.','code':0,'code2':2}
            return JsonResponse(message)
    except IndexError:
        message = {'alert': '비밀번호나 이메일을 입력해주세요 ','code':0,'code2':2}
        return JsonResponse(message)
    b = myemail.find('@')
    c = myemail.find('.')
    e = myemail.count('@')
    f = myemail.count('.')
    g = myemail.find(' ')
    cnt = 0
    if g == -1:
        if b == -1 or c ==-1:
            print('이메일 형식이 아닙니다')
            # @ . 없는경우
        elif b > c:
            print('이메일 형식이 아닙니다')
            # 바뀐경우
        elif b - c == -1 :
            print('이메일 형식이 아닙니다')
            # 사이에 문자가 없는경우
        elif e >= 2:
            print('이메일 형식이 아닙니다')
            # @2번이상
        elif f >= 2:
            print('이메일 형식이 아닙니다')
            # . 두번이상
        elif b == 0:
            print('이메일 형식이 아닙니다')
            # @ 앞에 문자
        elif c == 0:
            print('이메일 형식이 아닙니다')
            # . 앞에 문자
        else:
            print('이매일 확인')
            cnt = 1
    else:
        print('이메일 형식이 아닙니다')
    if hide_code == '1' and cnt == 0:
        message = {'alert': '이메일을 확인해주세요 \n admin@admin.~~ ', 'code': 0,'code2':2}
        return JsonResponse(message)
    elif hide_code == '1' and cnt == 1:
        message = {'alert': '회원가입 완료', 'code': 1,'code2':1}

        mymember = Mymember(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save()

        return JsonResponse(message)

    message = {'alert': '입력해주세요 ','code':0,'code2':2}
    return JsonResponse(message)

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
        if II.myname == user_id:
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

def getIn_score(request):
    confirm = ''
    fish_kind = request.GET['fish_kind']
    length = request.GET['length']
    score = request.GET['score']
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        myname = Mymember.objects.get(myname=user_id)
        if fish_kind == '광어':
            if myname.plaice is None:
                myname.plaice = 1
            else:
                myname.plaice =  myname.plaice+1
        elif fish_kind == '우럭':
            if myname.rockfish  is None:
                myname.rockfish  = 1
            else:
                myname.rockfish  =  myname.rockfish +1
        elif fish_kind == '감성돔':
            if myname.schlegelii  is None:
                myname.schlegelii  = 1
            else:
                print(myname.schlegelii )
                print(type(myname.schlegelii ))
                myname.schlegelii  =  myname.schlegelii +1
        elif fish_kind == '돌돔':
            if myname.striped_beakfish is None:
                myname.striped_beakfish = 1
            else:
                myname.striped_beakfish =  myname.striped_beakfish  +1
        elif fish_kind == '참돔':
            if myname.pagrus_major  is None:
                myname.pagrus_major = 1
            else:
                myname.pagrus_major =  myname.pagrus_major   +1

        myname.length =  length
        if myname.score is None:
            myname.score = int(score)
        else:
            myname.score = myname.score + int(score)

        myname.save()

    elif '_auth_user_id' in request.session:
        user_id = request.session['_auth_user_id']
        myname = Mymember.objects.get(myname=user_id)
        if fish_kind == '광어':
            if myname.plaice is None:
                myname.plaice = 1
            else:
                myname.plaice = myname.plaice + 1
        elif fish_kind == '우럭':
            if myname.rockfish is None:
                myname.rockfish = 1
            else:
                myname.rockfish = myname.rockfish + 1
        elif fish_kind == '감성돔':
            if myname.schlegelii is None:
                myname.schlegelii = 1
            else:
                myname.schlegelii = myname.schlegelii + 1
        elif fish_kind == '돌돔':
            if myname.striped_beakfish is None:
                myname.striped_beakfish = 1
            else:
                myname.striped_beakfish = myname.striped_beakfish + 1
        elif fish_kind == '참돔':
            if myname.pagrus_major is None:
                myname.pagrus_major = 1
            else:
                myname.pagrus_major = myname.pagrus_major + 1

        myname.length = length
        if myname.score is None:
            myname.score = int(score)
        else:
            myname.score = myname.score + int(score)

        myname.save()

    return HttpResponse(confirm)


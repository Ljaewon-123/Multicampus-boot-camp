from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02

def index(request):
    return render(request,'index.html')

def starbucks(reqeust):
    list_all = list()

    sido_all = starbucks02.getSiDo()  # 그냥 돌면 키만??
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_code=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_code=gugun)
                print(result)
                list_all.extend(result)
    # print(list_all)
    # print(len(list_all))

    result_dict = dict()
    result_dict['list'] = list_all

    return JsonResponse(result_dict)
    # JsonResponse() 안에 넣어주면 장고가 자동으로 json으로 바꿔줌
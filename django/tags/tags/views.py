from django.shortcuts import render


def index(request):
    return render(request,'index.html',{'name':'jaewon'})
#      그릴건데 render 응답받은 템플릿 파일에 변수에 jaewon 넣어줄거임

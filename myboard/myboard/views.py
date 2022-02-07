from django.shortcuts import render , redirect
from . models import MyBoard
from django.utils import timezone

def index(request):  # .order_by('-id')  원래 기본키로 오름차순을 하는데 '-'해서 내림차순으로
    return render(request,'index.html',{'list':MyBoard.objects.all()})
#  모델 객체를 가져올때 모델클래스명.objects. 으로 일단 찍고 본다
def insert_form(request):
    return render(request,'insert.html')

def insert_res(request):  # post에서 날린 데이터를 받는다 어떤 데이터를? 작성자,제목,내용
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname,mytitle=mytitle,mycontent=mycontent,mydate=timezone.now())
    # print(result)
    if result:
        return redirect('index')
    else:
        return redirect('insert')

def detail(request,id):
    return render(request,'detail.html',{'dto':MyBoard.objects.get(id=id)}) # 여기서 뭘 가지고 와야해?? id에 맞는 값!!

def update_form(request,id):
    return render(request,'update.html',{'dto':MyBoard.objects.get(id=id)})

def update_res(request):  # res는 뭘해야해?? update_form 의 id에 맞는 데이터를 보내 어디에?? insert랑 똑같? post방식 수신
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_update = myboard.update(mytitle=mytitle)
    result_update2 = myboard.update(mycontent=mycontent)
    print(type(result_update))
    print(result_update2)  # 수정한 개수 ?
    if result_update + result_update2 == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('update')

def delete(request,id):
    mydel = MyBoard.objects.get(id=id).delete()
    print(mydel)
    if mydel[0] :
        return redirect('index')
    else:
        return redirect('/detail/'+id)




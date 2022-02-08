from django.shortcuts import render , redirect
from . models import MyBoard , MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password , check_password
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import mimetypes

def index(request):  # .order_by('-id')  원래 기본키로 오름차순을 하는데 '-'해서 내림차순으로
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard,5)
    page_num = request.GET.get('page','1')  # 현재페이지 없으면 1로

    # 페이지에 맞는 모델 가져오기
    page_obj = paginator.get_page(page_num)  # get_page 메소드는 페이지 번호를 받아 해당 페이지를 리턴

    # 관련 매서드
    print(type(page_obj))
    print(page_obj.count)  # 총 객체수 (글 개수)
    print(page_obj.paginator.num_pages) # 총페이지 개수
    print(page_obj.paginator.page_range) # 페이지 번호 1부터 시작하는 범위? 리스트 반환?
    print(page_obj.has_next())            # 다음페이지 있으면 T 없으면 F
    print(page_obj.has_previous())        # 이전 페이지 있으면 T 없으면 F
    try:
        print(page_obj.next_page_number())   # 다음 페이지 번호
        print(page_obj.previous_page_number())  # 이전 페이지 번호
    except:
        pass
    print(page_obj.start_index())     # 시작번호
    print(page_obj.end_index())       # 끝번호

    return render(request,'index.html',{'list':page_obj})
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
    # print(type(result_update))
    # print(result_update2)  # 수정한 개수 ?
    if result_update + result_update2 == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('update')

def delete(request,id):
    mydel = MyBoard.objects.get(id=id).delete()
    # print(mydel)
    if mydel[0] :
        return redirect('index')
    else:
        return redirect('/detail/'+id)


def regitster(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        mymember = MyMember(myname = myname,mypassword=make_password(mypassword),myemail=myemail)
        mymember.save()

        return redirect('/')

    return redirect('/')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']

        mymember = MyMember.objects.get(myname = myname)

        if check_password(mypassword, mymember.mypassword):
            request.session['myname'] = mymember.myname
            return redirect('/')
        else:
            return redirect('/login')

def logout(request):
    del request.session['myname']  # 요청받으면 db에 있는 알맞는값 가져와서 세션에 저장 del하면 세션내용만 삭제
    return redirect('/')

def upload_process(request):
    upload_file = request.FILES['uploadfile']
    # print(upload_file)
    # print(type(upload_file))

    # setting에 있는 media 루트를 찾는다
    uploaded = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
    # print(uploaded)
    # print(type(uploaded))

    return render(request,'download.html',{'filename':uploaded})

def download_process(request,filename):
    mime_type = mimetypes.guess_type(filename)
    response = HttpResponse(default_storage.open(filename).read(),content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
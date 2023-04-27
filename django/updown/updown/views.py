import mimetypes

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def upload_process(request):
    upload_file = request.FILES['uploadfile']
    print(upload_file)
    print(type(upload_file))

    # setting에 있는 media 루트를 찾는다
    uploaded = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
    print(uploaded)
    print(type(uploaded))

    return render(request,'download.html',{'filename':uploaded})

def download_process(request,filename):
    mime_type = mimetypes.guess_type(filename)
    response = HttpResponse(default_storage.open(filename).read(),content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
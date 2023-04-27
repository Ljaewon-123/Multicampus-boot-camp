from django.contrib import admin
from . models import MyBoard,MyMember

admin.site.register(MyBoard)  # admin 사이트 에서 해당 모델 사용
admin.site.register(MyMember)

from django.urls import path

from . import views

urlpatterns = [
    # 왜 함수인데 index() 안붙임? 콜백 요청시에 처리되도록
    path('',views.index),
    path('test/',views.test),
    path('my/',views.my)
]
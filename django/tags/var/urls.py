from django.urls import path
from . import views

# {% url 'index' %} --> name='index'
urlpatterns = [
    path('',views.index,name='index'),
    path('var01/',views.variables01),
#     var urls 로 넘어가는 코드가 필요함  include
    path('var02/',views.variables02),
    path('forloop/',views.for_loop,name ='for'),
    path('if01/',views.if01),
    path('if02/',views.if02),
    path('href/',views.href),
    path('request/',views.get_post),
]

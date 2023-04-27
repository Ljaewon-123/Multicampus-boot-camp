"""pre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('clock/',views.clock),
    path('weather/',views.weather),
    path('weather/obs_weather/',views.obs_w),

    path('aa/',views.asdf),

    # 로그인 관련
    path('login_django/',views.login),
    path('logout_django/',views.logout),
    path('register/',views.regitster),
    path('register/double_check/', views.double_check),
    path('register/new_register/', views.new_register),

    # etc
    path('update_db/',views.update_db),
    path('get_in_score/',views.getIn_score),

    # 구글 로그인 관련

    # 구글
    path('accounts/',include('allauth.urls')),
]


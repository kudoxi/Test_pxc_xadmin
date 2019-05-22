from django.conf.urls import url
from . import views
from django.urls import path
# from apps.userinfo import viewUtil
from utils.validecode import *
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('usercenter/', views.usercenter, name="usercenter"),

    path('logout/', views.logout_, name="logout"),
    path('dologin/', views.dologin, name="dologin"),
    path('doregister/', views.doregister, name="doregister"),
    path('get_validcode_img/', get_validcode_img, name="get_validcode_img"),
    path('dopdf/', views.dopdf, name="dopdf"),
    path('email_valicode/', views.email_valicode, name="email_valicode"),
    #url(r'^get_validcode_img/', views.get_validcode_img,name="get_validcode_img"),

]
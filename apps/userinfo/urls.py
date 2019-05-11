from django.conf.urls import url
from . import views
from apps.userinfo import viewUtil

urlpatterns = [
    url('register/', views.register, name="register"),
    url('login/', views.login, name="login"),
    url('usercenter/', views.usercenter, name="usercenter"),

    url('logout/', views.logout_, name="logout"),
    url('dologin/', views.dologin, name="dologin"),
    url('doregister/', views.doregister, name="doregister"),
    url('get_validcode_img/', viewUtil.get_validcode_img, name="get_validcode_img"),
    url('dopdf/', views.dopdf, name="dopdf"),
    url('email_valicode/', views.email_valicode, name="email_valicode"),
    #url(r'^get_validcode_img/', views.get_validcode_img,name="get_validcode_img"),

]
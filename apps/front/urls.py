from django.conf.urls import url
from .views import *
from django.shortcuts import HttpResponse
def defalut(request):
    return HttpResponse(404)

urlpatterns = [
    url('^$', IdexView.index,name="index"),
    #url('test/', IdexView.test,name="test"),
    url('404/', defalut),
]
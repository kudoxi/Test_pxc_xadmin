from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^$', IdexView.index,name="index"),
    url('test/', IdexView.test,name="test"),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url('test/', views.test, name='test'),
    url('test_page/', views.test_page, name='test_page'),
    url('test_page_self/', views.test_page_self, name='test_page_self'),
    url('test_page_self2/(\w+)/', views.test_page_self2, name='test_page_self2'),
    #url('test_page_self3/(?P<a1>\w+)/(?P<a2>\w+)', views.test_page_self3, name='test_page_self3'),
    url('test_page_self4/(\w+)/(\w+)', views.test_page_self4, name='test_page_self4'),

    url('test_mark/', views.test_mark, name='test_mark'),


    url('test_mark2/(\d+)', views.test_mark2, name='aaa'),
    url('test_mark3/(?P<a1>\d+)/(?P<a2>\d+)', views.test_mark3, name='bbb'),

]
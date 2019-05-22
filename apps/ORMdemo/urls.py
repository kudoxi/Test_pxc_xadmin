from . import views
#from rest_framework import routers
#from ORMdemo.rest_views import UserViewSet
from django.urls import path
from django.conf.urls import url,include
#routers实例化
#router = routers.DefaultRouter()
#router.register(r'users',UserViewSet)

urlpatterns = [
    #path('api/',include(router.urls)),

    url('test/', views.test, name='test'),
    url('test_page/', views.test_page, name='test_page'),
    url('test_page_self/', views.test_page_self, name='test_page_self'),
    url('test_page_self2/(\w+)/', views.test_page_self2, name='test_page_self2'),
    #url('test_page_self3/(?P<a1>\w+)/(?P<a2>\w+)', views.test_page_self3, name='test_page_self3'),
    url('test_page_self4/(\w+)/(\w+)', views.test_page_self4, name='test_page_self4'),

    url('test_mark/', views.test_mark, name='test_mark'),


    url('test_mark2/(\d+)', views.test_mark2, name='aaa'),
    url('test_mark3/(?P<a1>\d+)/(?P<a2>\d+)', views.test_mark3, name='bbb'),
    #path('test_mark3/<int:a1>/<int:a2>', views.test_mark3, name='bbb'),

    #path('test_2/',views.test_2,name='test_2'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url('test/', views.test, name='test'),
    url('test_page/', views.test_page, name='test_page'),
    url('test_page_self/', views.test_page_self, name='test_page_self'),

    url('test_mark/', views.test_mark, name='test_mark')

]
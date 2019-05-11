# class MiddlewareMixin(object):
#     def __init__(self, get_response=None):
#         self.get_response = get_response
#         super(MiddlewareMixin, self).__init__()
#
#     def __call__(self, request):
#         response = None
#         if hasattr(self, 'process_request'):
#             response = self.process_request(request)
#         if not response:
#             response = self.get_response(request)
#         if hasattr(self, 'process_response'):
#             response = self.process_response(request, response)
#         return response

import sys
from django.views.debug import technical_500_response
from django.conf import settings
from django.http import HttpResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print("******in process_request")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('******in process view')#callback:视图函数 callback_args：参数
        print(callback, callback_args, callback_kwargs)
        return callback(request,*callback_args, **callback_kwargs)

    def process_response(self, request, response):
        print("******in process_response")
        return response

    def process_exception(self,request, exception):
        print("******in process_exception")

    def process_template_response(self,request,response):
        #对视图函数的返回值中，有render才调用y

        print("******in process_template_response")
        return response


class MyMiddleware2(MiddlewareMixin):
    def process_request(self,request):
        print("******in process_request2")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('******in process view2')

    def process_response(self, request, response):
        print("******in process_response2")
        return response

    def process_exception(self,request, exception):
        print("******in process_exception2")
        return HttpResponse('page error')

class UserBasedExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())
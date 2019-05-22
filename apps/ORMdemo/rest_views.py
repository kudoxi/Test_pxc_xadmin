from ORMdemo import models,rest_serializer
from rest_framework import routers,serializers,viewsets

#取出数据库数据，与序列化字段对应
class UserViewSet(viewsets.ModelViewSet):
    #queryset serializer_class是写死的字段名
    queryset = models.UserInfos.objects.all()
    serializer_class = rest_serializer.UserSerializer
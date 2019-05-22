from ORMdemo import models
from rest_framework import routers,serializers,viewsets

#序列化API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserInfos
        fields = ('name', 'age', 'ctime')
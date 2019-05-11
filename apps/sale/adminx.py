import xadmin
from .models import *

# 创建admin的管理类,这里不再继承自admin,而是object
class BrandAdmin(object):
    pass

class CarInfoAdmin(object):
    pass

xadmin.site.register(Brand,BrandAdmin)
xadmin.site.register(CarInfo,CarInfoAdmin)

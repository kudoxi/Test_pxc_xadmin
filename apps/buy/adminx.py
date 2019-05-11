import xadmin
from .models import *

# 创建admin的管理类,这里不再继承自admin,而是object
class CartAdmin(object):
    pass

class OrderAdmin(object):
    pass

xadmin.site.register(Cart,CartAdmin)
xadmin.site.register(Order,OrderAdmin)
import xadmin
from .models import *

# 创建admin的管理类,这里不再继承自admin,而是object
class BrandAdmin(object):
    pass

class CarInfoAdmin(object):
    # TODO 注意这里是remark字段是你要换成ueditor的字段，我这里就被坑了，好长时间不知道BUG出现在哪
    style_fields = {'remark': 'ueditor'}

xadmin.site.register(Brand,BrandAdmin)
xadmin.site.register(CarInfo,CarInfoAdmin)

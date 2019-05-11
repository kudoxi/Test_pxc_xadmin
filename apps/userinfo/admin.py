import xadmin
from .models import *
from xadmin.views import BaseAdminView,CommAdminView
# Register your models here.
#后台密码
#python
#tarena123
# xadmin.site.register(UserInfo)
# xadmin.site.register(DetailInfo)
# xadmin.site.register(Bank)
# xadmin.site.register(Message)
#
#
# class ThemeSetting(object):
#     # 主题功能开启
#     enable_themes = True
#     use_bootswatch = True
#
# class CustomView(object):
#     site_title = '庞械城后台管理'  #网页头部导航
#     site_footer = '苏州庞械城'   #底部版权
#     meun_style = 'accordion'   #左侧导航折叠筐
# # 将xadmin全局管理器与我们的view绑定注册
# xadmin.site.register(BaseAdminView, ThemeSetting)
# xadmin.site.register(CommAdminView,CustomView)
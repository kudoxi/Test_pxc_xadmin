import xadmin
from .models import *
from xadmin.views import BaseAdminView,CommAdminView
# Register your models here.
#后台密码 admin admin
#xadmin.sites.AlreadyRegistered: The model UserProfiles is already registered报错
xadmin.site.unregister(UserInfo)
class UserInfoAdmin(object):
    list_display = ['username', 'email', 'role', 'isActive', 'isBan']
    search_fields = ['email','role']  # 时间不做搜索
    list_filter = ['role', 'email'] #给后台添加一个过滤功能,可以通过这个过滤器来筛选出要显示的数据
xadmin.site.register(UserInfo,UserInfoAdmin)
#然后运行makemigrations xadmin
#migrate xadmin


xadmin.site.register(DetailInfo)
xadmin.site.register(Bank)
xadmin.site.register(Message)

class ThemeSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True

class CustomView(object):
    site_title = '庞械城后台管理'  #网页头部导航
    site_footer = '苏州庞械城'   #底部版权
    meun_style = 'accordion'   #左侧导航折叠筐

# 将xadmin全局管理器与我们的view绑定注册
xadmin.site.register(BaseAdminView, ThemeSetting)
xadmin.site.register(CommAdminView,CustomView)
from django.apps import AppConfig


class UserinfoConfig(AppConfig):
    name = 'apps.userinfo'
    verbose_name = '用户信息'  # 配置中文别名，还需在__init__中配置

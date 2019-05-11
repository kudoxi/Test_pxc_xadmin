from django.apps import AppConfig


class BuyConfig(AppConfig):
    name = 'apps.buy'
    verbose_name = '购买信息'  # 配置中文别名，还需在__init__中配置
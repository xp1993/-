from django.contrib import admin

# Register your models here.
from App.models import Goods

# 自定义站点
class MySite(admin.AdminSite):
    site_title = '爱鲜蜂'
    site_header = '爱鲜蜂数据管理后台'
    site_url = '/'
mysite = MySite()


# 商品的后台管理类
class GoodsAdmin(admin.ModelAdmin):

    # 检索字段
    search_fields = [
        'productlongname',
    ]

    # 要显式的字段
    list_display = [
        # 'productid',
        # 'productimg',
        # 'productname',
        'productlongname',
        'isxf',
        'pmdesc',
        'specifics',
        'price',
        'marketprice',
        'categoryid',
        # 'childcid',
        'childcidname',
        'dealerid',
        'storenums',
        'productnum',
        'onSale'
    ]

    # 分组过滤的字段
    list_filter = [
        # 'productlongname',
        'isxf',
        'pmdesc',
        'categoryid',
        'childcidname',
        'dealerid',
        # 'storenums',
        # 'productnum',
        'onSale',
    ]

    # 每页显式20条数据
    list_per_page = 20


mysite.register(Goods, GoodsAdmin)

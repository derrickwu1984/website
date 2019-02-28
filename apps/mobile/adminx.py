# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/2/28 9:19'
import  xadmin

from .models import custInfo
from xadmin import views

class BaseSetting(object):
    # 增加主题
    enable_themes=True
    # 主题样式集
    use_bootswatch=True
class GlobalSettings(object):
    # 修改header文字
    site_title="CBSS客户信息查询系统"
    # 修改footer文字
    site_footer = "兴磊互联网解决方案公司"
    # 收起默认菜单
    menu_style="accordion"

class custInfoAdmin(object):
    # 显示列表页展示项
    list_display=['phoneno','payname','querymonth','fee','actualbal',
                  'totalfee','actualfee','creditbal','openflag',
                  'custbrand','prodname','debtfee','paytype']
    search_fields=['querymonth','phoneno']
    list_filter=['phoneno','querymonth']
xadmin.site.register(custInfo,custInfoAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
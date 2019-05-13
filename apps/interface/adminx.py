# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/2/28 9:19'
import  xadmin

from .models import Details
from xadmin import views

class BaseSetting(object):
    # 增加主题
    enable_themes=True
    # 主题样式集
    use_bootswatch=True
class GlobalSettings(object):
    # 修改header文字
    site_title="企业网银接口查询系统"
    # 修改footer文字
    site_footer = "solution.inc"
    # 收起默认菜单
    menu_style="accordion"

class apiInfoAdmin(object):
    # 显示列表页展示项
    list_display=['trs_code','trs_name','fuc_desc']
    search_fields=['trs_code']
    list_filter=['trs_code']
xadmin.site.register(Details,apiInfoAdmin)
# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/2/28 9:19'
import  xadmin

from .models import custInfo

class custInfoAdmin(object):
    # 显示列表页展示项
    list_display=['phoneno','payname','querymonth','fee','actualbal',
                  'totalfee','actualfee','creditbal','openflag',
                  'custbrand','prodname','debtfee','paytype']
    search_fields=['querymonth','phoneno']
    list_filter=['phoneno','querymonth']
xadmin.site.register(custInfo,custInfoAdmin)
from django.db import models

# Create your models here.

class Details(models.Model):
    id = models.CharField(primary_key=True, max_length=200,default='', null=False)
    trs_code = models.CharField(max_length=20, default='', null=False, verbose_name='交易码')
    trs_name = models.CharField(max_length=200, default='', null=False, verbose_name='交易名称')
    fuc_desc = models.CharField(max_length=1000, default='', null=False, verbose_name='交易描述')
    flag = models.CharField(max_length=30, default='', null=False, verbose_name='输入输出标识')
    eng_name = models.CharField(max_length=200, default='', null=False, verbose_name='英文名')
    chinese_name = models.CharField(max_length=200, default='', null=False, verbose_name='中文名')
    data_type = models.CharField(max_length=20, default='', null=False, verbose_name='数据类型')
    required = models.CharField(max_length=200, default='', null=False, verbose_name='是否必输')
    remark  = models.CharField(max_length=2000, default='', verbose_name='备注')

    class Meta:
        verbose_name=u"接口详情"
        verbose_name_plural=verbose_name
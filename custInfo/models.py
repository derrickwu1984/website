#_*_encoding:utf-8_*_
from django.db import models

# Create your models here.
class custInfo(models.Model):
    object_id=models.CharField(max_length=64,default='',verbose_name='uuid',null=False,blank=True)
    crawldate=models.CharField(max_length=255,default='',verbose_name='信息获取日期',null=False,blank=True,primary_key=True)
    rangeno=models.CharField(max_length=10,default='',verbose_name='号段',null=False,db_index=True,blank=True)
    phoneno=models.CharField(max_length=11,verbose_name='手机号码',null=False,blank=True)
    paytype = models.CharField(max_length=255, verbose_name='付费类型',null=True,blank=True)
    querymonth=models.CharField(max_length=10,verbose_name='查询月份',null=True,blank=True)
    acctflag = models.CharField(max_length=255, verbose_name='账户标识',null=True,blank=True)
    debtfee=models.CharField(max_length=255,verbose_name='欠费金额',null=True,blank=True)
    fixtype = models.CharField(max_length=255, verbose_name='融合类型',null=True,blank=True)
    payname=models.CharField(max_length=255,verbose_name='付费名称',null=True,blank=True)
    prodname = models.CharField(max_length=255, verbose_name='产品名称',null=True,blank=True)
    fee=models.CharField(max_length=255,verbose_name='实时话费',null=True,blank=True)
    openflag = models.CharField(max_length=255, verbose_name='开通状态',null=True,blank=True)
    custbrand=models.CharField(max_length=255,verbose_name='客户品牌',null=True,blank=True)
    actualbal = models.CharField(max_length=255, verbose_name='实时结余',null=True,blank=True)
    custlocation=models.CharField(max_length=255,verbose_name='客户市县',null=True,blank=True)
    creditbal = models.CharField(max_length=255, verbose_name='信用额度',null=True,blank=True)
    totalfee=models.CharField(max_length=255,verbose_name='总计计费应收',null=True,blank=True)
    actualfee = models.CharField(max_length=255, verbose_name='总计实际应收',null=True,blank=True)

    class Meta:
        verbose_name=u"客户信息"
        verbose_name_plural=verbose_name

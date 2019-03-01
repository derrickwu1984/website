#_*_encoding：utf-8_*_
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import  datetime

# Create your models here.
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birthday=models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender=models.CharField(verbose_name=u"性别",choices=(("male","男"),("femal","女")),default="female",max_length=6)
    address=models.CharField(verbose_name=u"地址",max_length=100,default="")
    phoneno=models.CharField(max_length=11,null=True,blank=True)
    # image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name=u"用户信息"
        verbose_name_plural=verbose_name
    # 重载unicode，否则在print UserProfile实例的时候，不能打印自定义的字符串
    def __unicode__(self):
        return self.username
    pass
class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=10)
    # datetime.now() 是编译的时间 datetime.now 是class实例化的时间
    send_time=models.DateTimeField(default=datetime.now)


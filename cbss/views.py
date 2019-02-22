from django.shortcuts import render
from .models import mobile_userinfo_jinan
# Create your views here.
import  logging
def getList(request):
    # infoList=mobile_userinfo_jinan.objects.all()
    # for info in infoList:
    #     logging.warning(info.paytype)
    # return render(request, 'userInfoList.html')
    return render(request, 'index.html')

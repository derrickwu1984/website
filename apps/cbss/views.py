from django.shortcuts import render

# Create your views here.

def getList(request):
    return render(request,'userInfoList.html')

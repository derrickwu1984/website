from django.shortcuts import render
from .models import mobile_userinfo_jinan
# Create your views here.
import  logging
def indexPage(request):
    options = mobile_userinfo_jinan.objects.values("querymonth").distinct()
    return render(request, 'index.html', {
        "options":options
    })
def getList(request):
    if request.method == "POST":
        queryMonth=request.POST.get('queryMonth','')
        phoneNo = request.POST.get('phoneNo','')
        rangeNo=request.POST.get('rangeNo','')
        all_messages = mobile_userinfo_jinan.objects.filter(querymonth=queryMonth,rangeno=rangeNo)
        for message in all_messages:
            logging.warning(message.payname)
        return render(request, 'index.html', {
            "all_messages":all_messages
        })


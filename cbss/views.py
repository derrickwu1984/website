from django.shortcuts import render
from .models import mobile_userinfo_jinan
# Create your views here.
import  logging
def indexPage(request):
    return render(request, 'index.html')
def getList(request):
    if request.method == "POST":
        queryMonth=request.POST.get('queryMonth','')
        logging.warning(queryMonth)
        phoneNo = request.POST.get('phoneNo','')
        rangeNo=request.POST.get('rangeNo','')
        all_messages = mobile_userinfo_jinan.objects.filter(phoneno=phoneNo,querymonth=queryMonth,rangeno=rangeNo)
        for message in all_messages:
            logging.warning(message.payname)
    return render(request, 'result.html')



import  json
from django.shortcuts import render
from django.views.generic import View

from .models import Details,Header

def get_headers(request):
    api_headers = Header.objects.all()
    return render (request,"api_headers.html",{
        "api_headers":api_headers
    })
def get_params(request,trs_code):
    api_details = Details.objects.all()

    #取出接口号码
    if trs_code:
        api_details = api_details.filter(trs_code_id=trs_code)
    trs_name = list(api_details.values('trs_name').distinct())[0]['trs_name']
    fuc_desc =list(api_details.values('fuc_desc').distinct())[0]['fuc_desc']
    return render (request,"api_details.html",{
        "api_details":api_details,
        "trs_code":trs_code,
        "trs_name":trs_name,
        "fuc_desc":fuc_desc
    })

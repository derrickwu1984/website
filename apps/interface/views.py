
import  json
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Details,Header

def get_headers(request):
    # api_headers = Header.objects.all()
    infos = (Details.objects.values("trs_code","trs_name","fuc_desc").order_by("trs_code")).distinct()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    #Paginator(objects,per_page,request=request） per_page  不传就报错，代表每页显示条数
    p = Paginator(infos,10,request=request)
    all_info = p.page(page)
    return render (request,"api_headers.html",{
        "all_info":all_info
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

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入交易码'
        return render(request, "errors.html",{
            "error_msg": error_msg
        })
    result_list = (Details.objects.values("trs_code", "trs_name", "fuc_desc").filter(trs_code=q)).distinct()
    return render(request, "results.html", {
            "error_msg": error_msg,
            "result_list": result_list
    })
# 新增接口
def func_add(request):
    return render(request,"api_add.html")

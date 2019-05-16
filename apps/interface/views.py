
import  json,uuid
from django.shortcuts import render,HttpResponse
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Details,Header
from db.dbhelper import DBHelper

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
    return render (request, "api_detail.html", {
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
# 新增接口按钮
def interface_add(request):
    return render(request,"api_add.html")
#保存新增加接口数据
def save_record(request):
    params =[]
    if request.method=='POST':
         params =json.loads( request.POST.get('form_data'))
         for index_1 in range(len(params)):
            eng_name = params[index_1][0]
            chinese_name = params[index_1][1]
            data_type = params[index_1][2]
            remark = params[index_1][3]
            required = params[index_1][4]
            flag = params[index_1][5]
            trs_code = params[index_1][6]
            trs_name = params[index_1][7]
            fuc_desc = params[index_1][8]
            record = Details(id=str(uuid.uuid1()),trs_code_id=trs_code,trs_name=trs_name,fuc_desc=fuc_desc,flag=flag,eng_name=eng_name,chinese_name=chinese_name,data_type=data_type,required=required,remark=remark)
            record.save()
    return render(request,"api_headers.html")

#修改字段
def field_modify(request,trs_code):
    api_details = Details.objects.all()
    if trs_code:
        api_details = api_details.filter(trs_code_id=trs_code)
    trs_name = list(api_details.values('trs_name').distinct())[0]['trs_name']
    fuc_desc = list(api_details.values('fuc_desc').distinct())[0]['fuc_desc']
    return render(request, 'api_field_modify.html', {
        "api_details": api_details,
        "trs_code": trs_code,
        "trs_name": trs_name,
        "fuc_desc": fuc_desc
    })
#添加字段
def field_add(request,trs_code):
    api_details = Details.objects.all()
    if trs_code:
        api_details = api_details.filter(trs_code_id=trs_code)
    trs_name = list(api_details.values('trs_name').distinct())[0]['trs_name']
    fuc_desc = list(api_details.values('fuc_desc').distinct())[0]['fuc_desc']
    return render(request, 'api_field_add.html', {
        "api_details": api_details,
        "trs_code": trs_code,
        "trs_name": trs_name,
        "fuc_desc": fuc_desc
    })
#删除字段展示页面
def field_del(request,trs_code):
    api_details = Details.objects.all()
    if trs_code:
        api_details = api_details.filter(trs_code_id=trs_code)
    trs_name = list(api_details.values('trs_name').distinct())[0]['trs_name']
    fuc_desc = list(api_details.values('fuc_desc').distinct())[0]['fuc_desc']
    return render(request, 'api_field_del.html', {
            "api_details": api_details,
            "trs_code": trs_code,
            "trs_name": trs_name,
            "fuc_desc": fuc_desc
        })
#删除字段del逻辑
def field_del_save(request):
    if request.method == 'POST':
        delList = json.loads(request.POST.get('form_data'))
    idString = ','.join(delList)
    print (idString)
    # try:
    Details.objects.extra(where =["id IN ('"+idString+"')"]).delete()
        # print (record)
    # except:
    #     return HttpResponse('{"status":"fail", "msg":"数据删除失败"}', content_type='application/json')
    return HttpResponse('{"status":"success", "msg":"数据删除成功"}', content_type='application/json')

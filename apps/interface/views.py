
import  json,uuid,os
from django.shortcuts import render,HttpResponse
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Details
from db.dbhelper import DBHelper
from django.db import transaction
from .readUploadExcel import check_record,read_excel


def get_headers(request):
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
        api_details = api_details.filter(trs_code=trs_code)
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
    print (q)
    error_msg = ''
    if q=='':
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
            print (params[index_1])
            eng_name = params[index_1][0]
            chinese_name = params[index_1][1]
            data_type = params[index_1][2]
            remark = params[index_1][3]
            required = params[index_1][4]
            flag = params[index_1][5]
            trs_code = params[index_1][6]
            trs_name = params[index_1][7]
            fuc_desc = params[index_1][8]
            try:
                record = Details(id=str(uuid.uuid1()),trs_code=trs_code,trs_name=trs_name,fuc_desc=fuc_desc,flag=flag,eng_name=eng_name,chinese_name=chinese_name,data_type=data_type,required=required,remark=remark)
                record.save()
            except:
                return HttpResponse('{"status":"fail", "msg":"数据添加失败"}', content_type='application/json')
    return HttpResponse('{"status":"200", "msg":"数据添加成功"}', content_type='application/json')

#修改字段
def field_modify(request,trs_code):
    api_details = Details.objects.all()
    if trs_code:
        api_details = api_details.filter(trs_code=trs_code)
    trs_name = list(api_details.values('trs_name').distinct())[0]['trs_name']
    fuc_desc = list(api_details.values('fuc_desc').distinct())[0]['fuc_desc']
    return render(request, 'api_field_modify.html', {
        "api_details": api_details,
        "trs_code": trs_code,
        "trs_name": trs_name,
        "fuc_desc": fuc_desc
    })

# 保存修改字段信息
def field_modify_save(request):
    if request.method == 'POST':
        modifyList = json.loads(request.POST.get('form_data'))
        for i in range(len(modifyList)):
            eng_name = modifyList[i][0]
            chinese_name = modifyList[i][1]
            data_type = modifyList[i][2]
            remark = modifyList[i][3]
            required = modifyList[i][4]
            trs_code = modifyList[i][5]
            trs_name = modifyList[i][6]
            fuc_desc = modifyList[i][7]
            id = modifyList[i][8]
            flag = modifyList[i][9]
            # print (id,trs_code,trs_name,fuc_desc,eng_name,chinese_name,data_type,required,remark,flag)
            try:
                Details.objects.filter(id=modifyList[i][8]).update(
                    trs_code=trs_code,
                    trs_name=trs_name,
                    fuc_desc=fuc_desc,
                    eng_name=eng_name,
                    chinese_name=chinese_name,
                    data_type=data_type,
                    remark=remark,
                    required=required,
                    flag=flag
                )
            except:
                return HttpResponse('{"status":"fail", "msg":"数据修改失败"}', content_type='application/json')
        return HttpResponse('{"status":"200", "msg":"数据修改成功"}', content_type='application/json')


#添加字段
def field_add(request,trs_code):
    api_details = Details.objects.all()
    if trs_code:
        api_details = api_details.filter(trs_code=trs_code)
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
        api_details = api_details.filter(trs_code=trs_code)
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
        trs_code = request.POST.get('trs_code')
    for i in range(len(delList)):
        num =  Details.objects.filter(trs_code=trs_code).count()
        if (num>1):
            try:
                Details.objects.filter(id=delList[i]).delete()
            except:
                return HttpResponse('{"status":"fail", "msg":"数据删除失败"}', content_type='application/json')
        else:
            print ('else')
            return HttpResponse('{"status":"400", "msg":"该接口只剩下一个字段，不可以继续删除"}', content_type='application/json')
    return HttpResponse('{"status":"200", "msg":"数据删除成功"}', content_type='application/json')

def upload(request):
        return render(request,'excel_upload.html')

def excel_upload(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("没有文件需要上传!")
        destination = open(os.path.join("./upload/",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        trs_code=check_record()
        check_result = Details.objects.all().filter(trs_code=trs_code)
        if check_result:
           msg ="%s已存在，请在数据库中删除该接口信息后再重新上传"%trs_code
        else:
            result = read_excel()
            print(result)

            # msg ="%s不存在，可以上传"%trs_code
        return HttpResponse("文档上传成功！")
    else:
        return HttpResponse("文档上传没使用POST方法！")

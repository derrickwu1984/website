function createRow(obj) {
    node=''
    if (obj=='in'){
        node = 'content_in'
    }else {
        node = 'content_out'
    }
    var editTable = document.getElementById(node);
    var tr = document.createElement("tr");
    tr.classList.add("tr_class")
    var td0 = document.createElement("td");
    var checkbox=document.createElement("input");
	checkbox.type="checkbox";
	checkbox.name="checkRow";
	td0.appendChild(checkbox);
    var td1 = document.createElement("td");
    td1.innerHTML = "<input type='text' id='eng_name' name='eng_name' />";
    var td2 = document.createElement("td");
    td2.innerHTML = "<input type='text' id='chinese_name' name='chinese_name' />";
    var td3 = document.createElement("td");
    td3.innerHTML = "<input type='text' id='data_type' name='data_type' />";
    var td4 = document.createElement("td");
    td4.innerHTML = "<select id ='required' name='required'><option value='Y'>是</option><option value='N'>否</option></select>";
    var td5 = document.createElement("td");
    td5.innerHTML = "<input type='text' id='remark' name='remark'/>";
    var td6 = document.createElement("td");
    td6.innerHTML = "<input type='hidden' id='flag' name ='flag' value="+obj+"></input>";
    tr.appendChild(td0);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    editTable.appendChild(tr);
}
function delRow(obj) {
    node=''
    if (obj=='in'){
        node = 'content_in'
    }else {
        node = 'content_out'
    }
    var editTable = document.getElementById(node);
        var checkboxs = document.getElementsByName("checkRow");
        if (confirm("确认删除所选?")) {
        for (var i = 0; i < checkboxs.length; i++) {
            if (checkboxs[i].checked) {
                    var n = checkboxs[i].parentNode.parentNode;
                    editTable.removeChild(n);
                    i--;
                }
            }
        }
}
//obj区分是添加接口还是添加字段
function saveRecord(obj) {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    node =$('.tr_class')
    trs_code =$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
    trs_name =$('#trs_name').text()?$('#trs_name').text():$('#trs_name').val()
    fuc_desc =$('#fuc_desc').text()?$('#fuc_desc').text():$('#fuc_desc').val()
    var list=[]
    for (var i=0;i<node.length;i++){
        array=[]
        //提取<input type='text'/>元素
        input_tag =$(".tr_class:eq("+i+") td input:text")
        //提取<select/>元素
        select_tag_value =$(".tr_class:eq("+i+") td select").val()
        //提取<input type='hidden'/>元素
        input_hidden_tag =$(".tr_class:eq("+i+") td input:hidden").val()
        for (var j=0;j<input_tag.length;j++){
            array[j] =$(".tr_class:eq("+i+") input:text:eq("+j+") ").val()
            array[j+1]=select_tag_value
            array[j+2]=input_hidden_tag
            array[j+3]=trs_code
            array[j+4]=trs_name
            array[j+5]=fuc_desc
        }
        list.push(array)
    }
    var post_data= {
        "csrfmiddlewaretoken": token,
        "form_data": JSON.stringify(list)
    }
    // ajax将list发往后台
    $.ajax({
       	 url:"/save_record/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(result){
       	     if (result.status == 200){
       	         //如果是添加字段成功，路由到接口详情页:api_detail.html
       	         if(obj=='field'){
       	             alert(result.msg)
                     window.location.href="/trs_code/"+trs_code
                 }
                 //如果是添加接口成功，则路由到首页:api_headers.html
                 else {
       	             alert(result.msg)
                     window.location.href="/header/"
                 }
       	     }
       	     },
         error:function(result){
       	     if (result.status != 200){
       	         alert(result.msg)
                 window.location.href="/header/"
       	     }
         }
});
}
//修改字段
function updateRecord() {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    node =$('.tr_class')
    trs_code =$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
    trs_name =$('#trs_name').text()?$('#trs_name').text():$('#trs_name').val()
    fuc_desc =$('#fuc_desc').text()?$('#fuc_desc').text():$('#fuc_desc').val()
    var list=[]
    for (var i=0;i<node.length;i++){
        array=[]
        //提取<input type='text'/>元素
        input_tag =$(".tr_class:eq("+i+") td input:text")
        //提取<select/>元素
        select_tag_value =$(".tr_class:eq("+i+") td select").val()
        for (var j=0;j<input_tag.length;j++){
            array[j] =$(".tr_class:eq("+i+") input:text:eq("+j+") ").val()
            array[j+1]=select_tag_value
            array[j+2]=trs_code
            array[j+3]=trs_name
            array[j+4]=fuc_desc
        }
        //遍历<input type='hidden'/>元素,将value值push进array
        input_hidden_tag =$(".tr_class:eq("+i+") td input:hidden")
        for (var k=0;k<input_hidden_tag.length;k++){
            array.push($(".tr_class:eq("+i+") td input:hidden:eq("+k+") ").val())
        }
        list.push(array)
    }
    var post_data= {
        "csrfmiddlewaretoken": token,
        "form_data": JSON.stringify(list)
    }
    // ajax将list发往后台
    console.log(list)
    $.ajax({
       	 url:"/field_modify_save/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(result){
       	     if (result.status == '200'){
       	         alert(result.msg)
                 window.location.href="/trs_code/"+trs_code
       	     }
       	     },
         error:function(result){
       	     alert(result.msg)
       	     if (result.status != '200'){
       	         alert(result.msg)
       	     window.location.href="/header/"
       	     }
         }
});
}
function field_modify() {
    trs_code=$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
    $.ajax({
         url:"/field_modify/"+trs_code,
         type:"GET",
         async:"true",
        }
    )
}

function  delRecord() {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    trs_code=$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
    delList=[]
    if (confirm("确认删除所选?")) {
        $(':checkbox:checked').each(function(){
        var tr=$(this).closest('tr');
        v=tr.find('td:eq(6)').find('input').val();
            delList.push(v)
        })
    }
    var post_data= {
        "csrfmiddlewaretoken": token,
        "form_data": JSON.stringify(delList),
        "trs_code":trs_code
    }
    $.ajax({
       	 url:"/field_del_save/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(result){
       	     if (result.status == '200'||result.status == '400'){
       	         alert(result.msg)
                 window.location.href="/trs_code/"+trs_code
       	     }
       	     },
         error:function(result){
       	     if (result.status != '400' && result.status != '200'){
       	         alert(result.msg)
       	     window.location.href="/header/"
       	     }
         }
});
}

//接口详情页，增、删、改功能
function  change(obj) {
    if (obj=='header'||obj=='search'){
        window.location.href='/'+obj+'/'
    } else {
        trs_code=$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
        window.location.href='/'+obj+'/'+trs_code
    }
}
//首页搜索接口功能
function  search() {
    param=$("#q").text()?$("#q").text():$("#q").val()
    window.location.href='/search/?q='+param
}
//返回上一页
function goback() {
    trs_code=$('#trs_code').text()?$('#trs_code').text():$('#trs_code').val()
    window.location.href='/trs_code/'+trs_code
    
}
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

function saveRecord() {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    node =$('.tr_class')
    trs_code =$('#trs_code').val()?"":$('#trs_code').text()
    trs_name =$('#trs_name').val()?"":$('#trs_name').text()
    fuc_desc =$('#fuc_desc').val()?"":$('#fuc_desc').text()
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
    console.log(list)
    $.ajax({
       	 url:"/save_record/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(result){
       	     if (result.status == 200){console.log("接口添加成功^!^")}
       	     },
         error:function(result){
       	     if (result.status != 200){console.log("接口添加失败！")}
         }
});
}

function updateRecord() {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    node =$('.tr_class')
    trs_code =$('#trs_code').val()
    trs_name =$('#trs_name').val()
    fuc_desc =$('#fuc_desc').val()
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
    console.log(list)
    // ajax将list发往后台
    $.ajax({
       	 url:"/update_record/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(data){alert("接口修改成功^!^")},
         error:function(){alert("接口修改失败！")}
});
}
function field_modify() {
    trs_code=$("#trs_code").text()
    $.ajax({
         url:"/field_modify/"+trs_code,
         type:"GET",
         async:"true",
        }
    )
}

function  delRecord() {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    delList=[]
    if (confirm("确认删除所选?")) {
        $(':checkbox:checked').each(function(){
        var tr=$(this).closest('tr');
        v=tr.find('td:eq(6)').find('input').val();
            delList.push(v)
        })
    }
    console.log(delList)
    var post_data= {
        "csrfmiddlewaretoken": token,
        "form_data": JSON.stringify(delList)
    }
    $.ajax({
       	 url:"/field_del_save/",
         dataType:"JSON",
         type:"POST",
         async:"true",
         data:post_data,
         success:function(result){
       	     if (result.status == '200'){console.log("接口删除成功^!^")}
       	     },
         error:function(result){
       	     if (result.status != '200'){console.log("接口删除失败！")}
         }
});
}
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
        for (var i = 0; i < checkboxs.length; i++) {
            if (checkboxs[i].checked) {
                if (confirm("确认删除所选?")) {
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
    console.log(list)
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
         success:function(data){console.log('提交成功')},
         error:function(){console.log('提交失败！')}
});
}
$(document).ready(function() {
    $("#tablelist").dataTable({
        data: "",//为ajax的值,没有直接用插件自带的请求数据方式，个人觉得data的方式好控制一些
        columns: [{//设置表格内容
            sDefaultContent: "",//默认值
            data: "Id",//对应数据json的key
            bVisible: false //此列不显示
        }, {
            title: "名称",
            data: "Name",
            class:"",//设置当前td的class值
            render: function (data, type, full) { //自定义模块的内容，data为key对应的Name的值，full为所有的值
                return "<tr title='" + data + "' > " + data + "</tr>"; //可以通过设置div的宽来防止无法设置表格td的宽，并且可以添加title
            }
        }],
        //"columnDefs": [{//设置 编辑按钮
        //    "targets": [3],
        //    "data": "id",
        //    "render": function (data, type, full) {
        //        return "<a class='updata' href='#' >编辑</a>";
        //    }
        //}],
        bPaginate: true, //是否显示（应用）分页器
        bInfo: false, //是否显示页脚信息，DataTables插件左下角显示记录数
        bSort: true, //是否启动各个字段的排序功能
        aaSorting: [[0, 'asc']],//默认排序列
        bSelectAll: false,
        fnCallback: function () { },
        //oPageSize: 10,
        //oSortType: "desc",
        //oSortCol: "proName",
        bProcessing: true,
        oLanguage: {//多语言配置
            "sProcessing": "正在加载中......",
            "sLengthMenu": "每页显示 _MENU_ 条记录",
            "sZeroRecords": "对不起，查询不到相关数据！",
            "sEmptyTable": "表中无数据存在！",
            "sInfo": "当前显示 _START_ 到 _END_ 条，共 _TOTAL_ 条记录",
            "sInfoFiltered": "数据表中共为 _MAX_ 条记录",
            "sSearchPlaceholder": "🔍 查找",//搜索框内占位符
            "sSearch": "",//搜索框前的字体
            "oPaginate": {
                "sFirst": "首页",
                "sPrevious": "上一页",
                "sNext": "下一页",
                "sLast": "末页"
            }
        }
    });
});
//$(".tabel").dataTable({aaData : d});//重新加载数据
//$(".table").dataTable().fnDeleteRow(index);//删除行
//$(".table").dataTable().fnUpdate("a", 1, 1, false);//修改行,最后一个参数，是否重绘表格
//$(".table").dataTable().fnUpdate(["a","b"],1);//修改列
//$(".table").DataTable().row.add(dc).draw();//添加行
//$(".table").dataTable().fnPageChange(page); //跳转到某页
//$(".table").dataTable().fnGetData();//得到页面中所有对象
//$(".table").dataTable().fnSetColumnVis( 0, false);//隐藏列
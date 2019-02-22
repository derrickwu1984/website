var data = [
    {id:1,text:'201901'},
    {id:2,text:'201902'},
    {id:3,text:'201903'},
    {id:4,text:'201904'},
    {id:5,text:'201905'},
    {id:6,text:'201906'},
    {id:7,text:'201907'},
    {id:8,text:'201908'},
    {id:9,text:'201909'},
    {id:10,text:'201910'},
    {id:11,text:'201911'},
    {id:12,text:'201912'}
];
$(document).ready(function () {
    $('.js-example-basic-single').select2({
        placeholder:"请选择月份",
        data:data,
        allowClear:true,
        maximumSelectionLength:2,
        tags:true,
        language:'zh-CN'
    });
});
function onclick() {
    var data=[];
    var datalist=[];
    data= $('.js-example-basic-single').select2("data");
    data.forEach(function (item) {
        datalist.push(item.text);
    })
    console.log("你选择的是:"+datalist)
}
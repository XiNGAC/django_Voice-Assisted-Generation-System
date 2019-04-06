function submit_recognition(table){
    var table_name = 'recognition_' + table;
    var tb = document.getElementById(table_name);
    var row_num = tb.rows.length;
    alert(row_num);
    for(var i = 1; i <row_num; i++)
    {
        tb.deleteRow(i);
        row_num=row_num-1;
        i=i-1;
    }
    var input_str = 'translate_to_word_'+table;
    var input_text = document.getElementById(input_str).value;
    var str_url = "/a_recognition_submit_"+ table;
    $.ajax({
       type : "post",
       url : str_url,
       datatype : "json",
       data: {
           report_input : input_text
       },
       success: function (data) {
           // console.info(data);
           alert(data[1]);
           var tab = document.getElementById(table_name);
           for(var j = 0,len = data.length; j < len; j++){
               console.log(data[j]);
               var newTR = tab.insertRow(tab.rows.length);
               var new1 = newTR.insertCell();
               var new2 = newTR.insertCell();
               var new3 = newTR.insertCell();
               var new4 = newTR.insertCell();
               var new5 = newTR.insertCell();
               new1.innerText = j+1;
               new2.innerText = data[j][0];
               new3.innerText = data[j][1];
               new4.innerText = data[j][2];
               new5.innerText = data[j][3];

           }
           var result_str = 'result_translate_to_word_'+table;
           // document.getElementById(result_str).value= data;
       }
    });
    // alert('1');
}

function submit_extraction(){
    var input_text = document.getElementById('translate_to_word').value;
    $.ajax({
       type : "post",
       url : "/a_extraction_submit",
       datatype : "json",
       data: {
           report_input : input_text
       },
       success: function (data) {
           console.info(data);
           // alert(data);
           document.getElementById('result_translate_to_word').value= data;
       }
    });
    // alert('1');
}

function submit_diagnosis(){
    var input_text = document.getElementById('translate_to_word').value;
    $.ajax({
       type : "post",
       url : "/a_diagnosis_submit",
       datatype : "json",
       data: {
           report_input : input_text
       },
       success: function (data) {
           console.info(data);
           // alert(data);
           document.getElementById('result_translate_to_word').value= data;
       }
    });
    // alert('1');
}

// $("#upload_file").click(function(){//点击导入按钮，使files触发点击事件，然后完成读取文件的操作。
// //         $("#choose_files").click();
// //         alert('click')
// //     });

function click_upload_button(table) {
    var name = "#xdaTanFileImg_"+table;
    $(name).click();
}

function upload_file_to_textarea(){
    var selectedFile = document.getElementById("choose_files").files[0];//获取读取的File对象
    var name = selectedFile.name;//读取选中文件的文件名
    var size = selectedFile.size;//读取选中文件的大小
    console.log("文件名:"+name+"大小："+size);
    var reader = new FileReader();//这里是核心！！！读取操作就是由它完成的。
    reader.readAsText(selectedFile);//读取文件的内容

    reader.onload = function(){
        console.log(this.result);//当读取完成之后会回调这个函数，然后此时文件的内容存储到了result中。直接操作即可。
        document.getElementById('translate_to_word').value=this.result;
    };
}

function xmTanUploadImg(obj,table) {
    var file = obj.files[0];
    console.log(obj);console.log(file);
    console.log("file.size = " + file.size);  //file.size 单位为byte
    var reader = new FileReader();
    //读取文件过程方法
    reader.onload = function (e) {
        console.log("成功读取....");
        var name = "xmTanImg_"+table;
        var img = document.getElementById(name);
        img.src = e.target.result;
        //或者 img.src = this.result;  //e.target == this
    };
    reader.readAsDataURL(file);
    var ocr_name = 'run_ocr_'+table;
    document.getElementById(ocr_name).style.display = 'block';
}

function run_ocr(table) {
    var input = 'xmTanImg_'+table;
    var image_info = document.getElementById(input);
    var temp = image_info.src;
    console.log(temp);
    var reg = /base64,(\S*)/;
    var reg_match = temp.match(reg)[1];
    console.log(reg_match);
    $.ajax({
       type : "post",
       url : "/run_ocr",
       datatype : "json",
       data: {
           base64_pic : reg_match
       },
       success: function (data) {
           console.info(data);
           // alert(data);
           var name = 'translate_to_word_'+table;
           document.getElementById(name).value= data;
       }
    });
}

function create_patient () {
    var name = document.getElementById("p_name").value;
    var sex = document.getElementById("p_sex").value;
    var age = document.getElementById("p_age").value;
    if(name=='' || age==''){
        document.getElementById('p_save_notice_error').style.display="block";
        document.getElementById('p_save_notice').style.display="none";
    }
    else{
        document.getElementById('p_save_notice_error').style.display="none";
        document.getElementById('p_save_noticing').style.display="block";
        $.ajax({
       type : "post",
       url : "/insert_patient",
       datatype : "json",
       data: {
           name: name,
           sex: sex,
           age: age
       },
       success: function () {
           document.getElementById('p_save_noticing').style.display="none";
           document.getElementById('p_save_notice').style.display="block";
       }
    });
    }
}

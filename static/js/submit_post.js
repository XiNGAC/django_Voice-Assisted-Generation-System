function submit_recognition(){
    var input_text = document.getElementById('translate_to_word').value;
    $.ajax({
       type : "post",
       url : "/a_recognition_submit",
       datatype : "json",
       data: {
           report_input : input_text
       },
       success: function (data) {
           console.info(data);
           alert(data);
           document.getElementById('result_translate_to_word').value= data;
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
           alert(data);
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
           alert(data);
           document.getElementById('result_translate_to_word').value= data;
       }
    });
    // alert('1');
}

// $("#upload_file").click(function(){//点击导入按钮，使files触发点击事件，然后完成读取文件的操作。
// //         $("#choose_files").click();
// //         alert('click')
// //     });

function click_upload_button() {
    $("#choose_files").click();
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
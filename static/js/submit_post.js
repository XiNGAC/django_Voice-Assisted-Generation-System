function submit_recognition(){
    var input_text = document.getElementById('translate_to_word').value;
    $.ajax({
       type : "post",
       url : "/a_report_input_submit",
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
    alert('1');
}
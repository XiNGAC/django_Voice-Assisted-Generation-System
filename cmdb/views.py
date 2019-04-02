from django.shortcuts import render, redirect

from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import os
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from django.forms import fields
from django import forms
from cmdb.models import ReportDetail, NormalInfo, ChangeInfo, Patient
import json
import re
import pymysql
from aip import AipSpeech
import codecs
import hashlib
import base64
import urllib
from urllib import parse
import time
import urllib.request
import requests
import pdfkit
from wkhtmltopdf.views import PDFTemplateView
from core import MainFunction
from core import LSTM_CRF
from core import insert_sql


from aip import AipSpeech
import  wave
import threading
import tkinter.filedialog
import tkinter.messagebox
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import time

# Create your views here.

inputReportList = [
]



class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    email = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密_码')
    # password1 = forms.CharField(label='xxx')
    confirm = forms.CharField(label='确_认')


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("hello world")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
    return render(request, "index.html",)


def test(request):
    return render(request, "test.html", {'lst': inputReportList})


def creat_patient(request):
    return render(request, "creat_patient.html", )


def pdf(request):
    # p_name = temp_json['table_patient_name']
    # p_sex = temp_json['table_patient_sex']
    # p_age = temp_json['table_patient_age']
    # p_id = temp_json['table_patient_id']
    p_name = 'zs'
    p_sex = '男'
    p_age = '30'
    p_id = '1'
    tempDic = {'p_name': p_name, 'p_sex': p_sex, 'p_age': p_age, 'p_id': p_id}
    return render(request, "pdf.html")


def forms(request):
    return render(request, "forms.html",)


def check_report(request):
    inputReportList=[]
    pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    f = open(pwd + "/mysite/static/pdf/report_list.txt", 'r')
    for line in f:
        print(line)
        temp = json.loads(line)
        tempReportInfo = {'id': temp['id'], 'name': temp['name'], 'check': temp['check'], 'date': temp['date'], 'report': temp['report']}
        inputReportList.append(tempReportInfo)
    print(inputReportList)
    return render(request, "check_report.html", {'lst': inputReportList},)


def a_report_input(request):
    pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    f = open(pwd + "/mysite/static/check_num.txt", 'r')
    check_num = f.read()
    print(check_num)
    return render(request, "a_report_input.html",{'check_num':check_num})


def a_recognition(request):
    return render(request, "a_recognition.html",)


def a_recognition_submit_table1(request):
    if request.method == "POST":
        input_str = request.POST.get("report_input")
        print(input_str)
    # print('helloworld')
    result_str = LSTM_CRF.evaluate_line(input_str)
    # result_str = 'TABLE1: recognition submit as '+input_str
    print(result_str['entities'])
    return JsonResponse(str(result_str['entities']), safe=False)


def a_recognition_submit_table2(request):
    if request.method == "POST":
        input_str = request.POST.get("report_input")
        print(input_str)
    print('helloworld')
    result_str = 'TABLE2: recognition submit as '+input_str
    print(result_str)
    return JsonResponse(result_str, safe=False)


def a_extraction(request):
    return render(request, "a_extraction.html",)


def a_extraction_submit(request):
    if request.method == "POST":
        input_str = request.POST.get("report_input")
        print(input_str)
    print('helloworld')
    result_str = 'extration submit as '+input_str
    print(result_str)
    return JsonResponse(result_str, safe=False)


def a_diagnosis(request):
    return render(request, "a_diagnosis.html",)


def a_diagnosis_submit(request):
    if request.method == "POST":
        input_str = request.POST.get("report_input")
        print(input_str)
    print('helloworld')
    result_str = 'diagnosis submit as '+input_str
    print(result_str)
    return JsonResponse(result_str, safe=False)


def registered(request):
    return render(request, 'registered.html')


def register(request):
    print('0')
    message=""
    if request.method == 'POST':
        print('00')
        message = "检查填写内容"
        uf = UserForm(request.POST)
        print(uf)
        if uf.is_valid():
            print('xx')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm = request.POST.get('confirm')
            print(username, email, password, confirm)
            if password != confirm:
                message = "两次输入的密码不同！"
                print('1')
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = "用户名已存在"
                    print('2')
                    return render(request, 'register.html', locals())
            register_add = User.objects.create_user(username=username, email=email, password=password)
            print('add')
            re = auth.authenticate(username=username, password=password)
            message = "注册成功"
            if register_add == False:
                print('3')
                return render(request, 'share1.html', {'registAdd': register_add, 'username': username})
            else:
                auth.login(request, re)
                print(register_add)
                return redirect("/index", {'user': re})
    else:
        uf = UserForm()
        print('4')
    # return HttpResponse(message)
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        re = auth.authenticate(username=username, password=password)
        if re is not None:
            auth.login(request, re)
            print(re)
            return redirect("/a_report_input", {'user': re})
        else:
            return render(request, 'login.html', {'login_error': '用户名或密码错误'})
    return render(request, "login.html",)


def logout(request):
    auth.logout(request)
    return render(request, "index.html")


def xx(request):
    return render(request, "to_use_py_test.html",)


def xxx(request):
    return JsonResponse("", safe=False)


def audio_test(request):
    return render(request, "audio_test.html",)


@csrf_exempt
def ajax_patient(request):
    with connection.cursor() as c:
        c.execute("select patient_name,patient_sex, patient_age,patient_id from patient")
        patients = c.fetchall()
        print(patients)
    return JsonResponse(patients, safe=False)


def ajax_patient_info(request):
    with connection.cursor() as c:
        c.execute("select patient_name,patient_sex,patient_age,patient_id from patient where patient_name=%s" [p_name])
        patient_info = c.fetchall()
    return JsonResponse(patient_info, safe=False)


def ajax_report_detail(request):
    model1 = {"左叶":
                  {"大小":
                       {"前后径": "", "左右径": ""},
                   "形态": "",
                   "回声": "",
                   "回声分布": "",
                   "边界": "",
                   "表面": "",
                   "包膜": "",
                   "CDFI": ""
                   },
              "右叶":
                  {"大小": {"前后径": "", "左右径": ""},
                   "形态": "",
                   "回声": "",
                   "回声分布": "",
                   "边界": "",
                   "表面": "",
                   "包膜": "",
                   "CDFI": ""
                   },
              "峡部": ""
              }
    parameter1 = {"形态": r"形态(.+)", "前后径": r"前后径(.+)", "左右径": r"左右径(.+)", "回声分布": r"回声分布(.+)"
        , "回声": r"内部(.+)回声", "峡部": r"峡部(.+)", "表面": r"表面(.+)、",
                  "包膜": r"包膜(.+)", "边界": r"边界(.+)", "CDFI": r"CDFI(.+)"}
    model2 = model = {"左侧":
        {
            "位置补充": "",
            "甲状腺": "",
            "可见": "",
            "大小": "",
            "生长": "",
            "形状": "",
            "边缘": "",
            "边界": "",
            "内部回声": "",
            "内部结构": "",
            "后方回声": "",
            "FI": "",
            "钙化": "",
            "补充": "",
            "强回声": "",
            "声影": "",
            "声晕": ""
        },
        "右侧":
            {
                "位置补充": "",
                "甲状腺": "",
                "可见": "",
                "大小": "",
                "生长": "",
                "形状": "",
                "边缘": "",
                "边界": "",
                "内部回声": "",
                "内部结构": "",
                "后方回声": "",
                "FI": "",
                "钙化": "",
                "补充": "",
                "强回声": "",
                "声影": "",
                "声晕": ""
            },
        "双侧":
            {
                "左侧": {
                    "大小": "",
                    "位置补充": ""
                },
                "右侧": {
                    "大小": "",
                    "位置补充": ""
                },
                "甲状腺": "",
                "可见": "",
                "生长": "",
                "形状": "",
                "边缘": "",
                "边界": "",
                "内部回声": "",
                "内部结构": "",
                "后方回声": "",
                "FI": "",
                "钙化": "",
                "补充": "",
                "强回声": "",
                "声影": "",
                "声晕": ""
            },
        "峡部":
            {
                "位置补充": "",
                "甲状腺": "",
                "可见": "",
                "大小": "",
                "生长": "",
                "形状": "",
                "边缘": "",
                "边界": "",
                "内部回声": "",
                "内部结构": "",
                "后方回声": "",
                "FI": "",
                "钙化": "",
                "补充": "",
                "强回声": "",
                "声影": "",
                "声晕": ""
            },
    }
    parameter2 = {"甲状腺": r".+甲状腺.+?可见.+?个(.+)", "可见": r"可见(.+)个", "大小": r"大小(.+)", "生长": r"(.+)生长", "形状": r"形状(.+)"
        , "边缘": r"边缘(.+)", "边界": r"边界(.+)", "内部回声": r"内部回声(.+)", "内部结构": r"内部结构(.+)",
                  "后方回声": r"后方回声(.+)", "FI": r"FI(.+)", "钙化": r"(.+)钙化", "强回声": r"(.+)强回声", "声晕": r"(.+)声晕",
                  "声影": r"(.+)声影"}
    reportlist = ""
    MainFunction.splitTable()
    part1Res =MainFunction.part1Construct(model1, parameter1)
    part2Res =MainFunction.part2Construct(model2, parameter2)
    print(json.dumps(part1Res, ensure_ascii=False))
    print(json.dumps(part2Res, ensure_ascii=False))

    # insert_sql.insert(part1Res, part2Res)

    with connection.cursor() as c:
        c.execute("select * from report_detail where report_id = '1'")
        temp = c.fetchall()
        report_detail = list(temp)
        c.execute("select * from normal_info where normal_id = '%s'" % (report_detail[0][11])) #右侧基本
        temp = c.fetchall()
        report_detail.append(list(temp)[0])
        c.execute("select * from normal_info where normal_id = '%s'" % (report_detail[0][12])) #左侧基本
        temp = c.fetchall()
        report_detail.append(list(temp)[0])
        c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][13])) #右侧局灶
        temp = c.fetchall()
        report_detail.append(list(temp)[0])
        c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][14]))  # 左侧局灶
        temp = c.fetchall()
        report_detail.append(list(temp)[0])
        c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][15]))  # 峡部局灶
        temp = c.fetchall()
        report_detail.append(list(temp)[0])
        # print(report_detail[0][11])
        print(report_detail)
        print(type(report_detail))
    return JsonResponse(report_detail, safe=False)


def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        file = request.FILES.get("myfile", None)
        if file is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
            # pwd = os.path.dirname(__file__)
            print(pwd)
            with open(pwd+"/mysite/static/radio/%s.wav" % file.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in file.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, 'upload.html')


def run_py(request):
    if request.method == "POST":
        # os.system('D:\\python\\python.exe E:\\workspace_django\\mysite\\static\\py\\audio_transfer.py')
        # os.system('D:\\python\\python.exe E:\\workspace_django\\mysite\\static\\py\\word_cut_test.py')
        pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

        f = open(pwd+"/mysite/static/radio/test1.wav", 'rb')
        file_content = f.read()
        base64_audio = base64.b64encode(file_content)
        body = parse.urlencode({'audio': base64_audio})

        url = 'http://api.xfyun.cn/v1/service/v1/iat'
        api_key = '9550b1014a2275ec83cf7eb72255db51'
        param = {"engine_type": "sms16k", "aue": "raw"}

        x_appid = '5c622e5b'
        json_str = json.dumps(param).replace(' ', '')
        print('json_str:{}'.format(json_str))
        x_param = base64.b64encode(bytes(json_str, 'ascii'))
        x_time = int(int(round(time.time() * 1000)) / 1000)
        x_checksum_str = api_key + str(x_time) + str(x_param)[2:-1]
        print('x_checksum_str:[{}]'.format(x_checksum_str))
        x_checksum = hashlib.md5(x_checksum_str.encode(encoding='ascii')).hexdigest()
        print('x_checksum:{}'.format(x_checksum))
        x_header = {'X-Appid': x_appid,
                    'X-CurTime': x_time,
                    'X-Param': x_param,
                    'X-CheckSum': x_checksum}

        start_time = time.time()
        req = urllib.request.Request(url, bytes(body, 'ascii'), x_header)
        result = urllib.request.urlopen(req)
        result = result.read()
        print("used time: {}s".format(round(time.time() - start_time, 2)))
        print('result:' + str(result.decode(encoding='UTF8')))
        Jsondata = json.loads(result)
        print(type(Jsondata))
        string = ''.join(Jsondata['data'])
        return JsonResponse(Jsondata['data'], safe=False)


        # return render(request, 'a_report_input.html')


def run_ocr(request):
    if request.method == "POST":
        f1_base64 = request.POST.get('base64_pic')
        URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/general"
        APPID = "5c622e5b"
        API_KEY = "20bc07cde0928d61e5c92b5867ab01fe"
        curTime = str(int(time.time()))
        param = {"language": "cn|en", "location": "false"}
        param = json.dumps(param)
        paramBase64 = base64.b64encode(param.encode('utf-8'))

        m2 = hashlib.md5()
        str1 = API_KEY + curTime + str(paramBase64, 'utf-8')
        m2.update(str1.encode('utf-8'))
        checkSum = m2.hexdigest()

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }

        data = {
            'image': f1_base64
        }

        r = requests.post(URL, data=data, headers=header)
        result = str(r.content, 'utf-8')
        jsondata = json.loads(result)
        print(jsondata)
        str_data=json.dumps(jsondata,ensure_ascii=False)
        refind = re.findall("{\"content\": \"(.*?)\"}", str_data)
        print(refind)
        print(type(refind))
        result_data = ''
        result_data = result_data.join(refind)
        # resultdata = jsondata['data']['block'][0]['line'][0]['word'][0]['content']
        print(result_data)
        # str_list = ['Python', 'Tab']
        # a = ''
        # print(a.join(refind))
        return JsonResponse(result_data, safe=False);


def insert_into_mysql(request):
    if request.method == "POST":
        print((request.POST.get('string')))
        #print(json.loads(request.POST.get('string'))['table_patient_id'])
        temp_json = json.loads(request.POST.get('string'))
        # {'table_patient_id': '0'},
        patient_id = temp_json['table_patient_id']
        department_name = temp_json['department_name']
        door_number = temp_json['door_number']
        check_number = temp_json['check_number']
        check_item = temp_json['check_item']
        machine_number = temp_json['machine_number']
        size_thickness = temp_json['size_thickness']
        diagnosis = temp_json['diagnosis']
        review_physician = temp_json['review_physician']
        check_date = temp_json['check_date']
        nr_id = temp_json['nr_id']
        nr_id = NormalInfo.objects.get(normal_id=int(nr_id))
        nl_id = temp_json['nl_id']
        nl_id = NormalInfo.objects.get(normal_id=int(nl_id))
        cr_id = temp_json['cr_id']
        cr_id = ChangeInfo.objects.get(change_id=int(cr_id))
        cl_id = temp_json['cl_id']
        cl_id = ChangeInfo.objects.get(change_id=int(cl_id))
        ct_id = temp_json['ct_id']
        ct_id = ChangeInfo.objects.get(change_id=int(ct_id))
        # print(nr_id,nl_id,cr_id)
        create = ReportDetail.objects.create(patient_id=patient_id, department_name=department_name,
                                             check_number=check_number, clinic_number=door_number,
                                             check_item=check_item, machine_number=machine_number,
                                             size_thickness=size_thickness, diagnosis=diagnosis,
                                             review_physician=review_physician, check_date=check_date,
                                             normal_right=nr_id, normal_left=nl_id, change_thickness=ct_id,
                                             change_right=cr_id, change_left=cl_id)
        print(type(create), create)
        return JsonResponse(temp_json, safe=False)


def insert_patient(request):
    if request.method == 'POST':
        name = (request.POST.get('name'))
        if request.POST.get('sex')=='男':
            sex = 1
        else:
            sex = 2
        age = (request.POST.get('age'))
        create = Patient.objects.create(patient_name=name, patient_age=age, patient_sex=sex)
        print(type(create),create)
        return JsonResponse('1', safe=False)


def save_pdf(request):
    result = 'error'
    if request.method == "POST":
        temp_json = json.loads(request.POST.get('string'))
        # print(temp_json)
        p_name = temp_json['table_patient_name']
        p_sex = temp_json['table_patient_sex']
        p_age = temp_json['table_patient_age']
        p_id = temp_json['table_patient_id']
        p_department = temp_json['department_name']
        p_clinic = temp_json['door_number']
        p_check_num = temp_json['check_number']
        p_check_item = temp_json['check_item']
        p_machine = temp_json['machine_number']
        p_thickness_size = temp_json['size_thickness']
        p_diagnosis = temp_json['diagnosis']
        review_physician = temp_json['review_physician']
        check_date = temp_json['check_date']
        # print(p_name, p_sex, p_age, p_id)

        with connection.cursor() as c:
            c.execute("select * from report_detail where report_id = '1'")
            temp = c.fetchall()
            report_detail = list(temp)
            c.execute("select * from normal_info where normal_id = '%s'" % (report_detail[0][11]))  # 右侧基本
            temp = c.fetchall()
            report_detail.append(list(temp)[0])
            c.execute("select * from normal_info where normal_id = '%s'" % (report_detail[0][12]))  # 左侧基本
            temp = c.fetchall()
            report_detail.append(list(temp)[0])
            c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][13]))  # 右侧局灶
            temp = c.fetchall()
            report_detail.append(list(temp)[0])
            c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][14]))  # 左侧局灶
            temp = c.fetchall()
            report_detail.append(list(temp)[0])
            c.execute("select * from change_info where change_id = '%s'" % (report_detail[0][15]))  # 峡部局灶
            temp = c.fetchall()
            report_detail.append(list(temp)[0])

        p_r_fb = report_detail[1][1]
        p_r_lr = report_detail[1][2]
        p_r_shape = report_detail[1][3]
        p_r_echo = report_detail[1][4]
        p_r_echo_d = report_detail[1][5]
        p_r_edge = report_detail[1][6]
        p_r_surface = report_detail[1][7]
        p_r_envelope = report_detail[1][8]
        p_r_cdfi = report_detail[1][9]
        p_l_fb = report_detail[2][1]
        p_l_lr = report_detail[2][2]
        p_l_shape = report_detail[2][3]
        p_l_echo = report_detail[2][4]
        p_l_echo_d = report_detail[2][5]
        p_l_edge = report_detail[2][6]
        p_l_surface = report_detail[2][7]
        p_l_envelope = report_detail[2][8]
        p_l_cdfi = report_detail[2][9]
        p_cr_position = report_detail[3][1]
        p_cr_type = report_detail[3][2]
        p_cr_num = report_detail[3][3]
        p_cr_size = report_detail[3][4]
        p_cr_grow = report_detail[3][5]
        p_cr_shape = report_detail[3][6]
        p_cr_edge = report_detail[3][7]
        p_cr_boundary = report_detail[3][8]
        p_cr_echo_inside = report_detail[3][9]
        p_cr_structure = report_detail[3][10]
        p_cr_echo_back = report_detail[3][11]
        p_cr_cdfi = report_detail[3][12]
        p_cr_cal = report_detail[3][13]
        p_cr_echo_strong = report_detail[3][14]
        p_cr_sound = report_detail[3][15]
        p_cr_halo = report_detail[3][16]
        p_cr_supplement = report_detail[3][17]
        p_cl_position = report_detail[4][1]
        p_cl_type = report_detail[4][2]
        p_cl_num = report_detail[4][3]
        p_cl_size = report_detail[4][4]
        p_cl_grow = report_detail[4][5]
        p_cl_shape = report_detail[4][6]
        p_cl_edge = report_detail[4][7]
        p_cl_boundary = report_detail[4][8]
        p_cl_echo_inside = report_detail[4][9]
        p_cl_structure = report_detail[4][10]
        p_cl_echo_back = report_detail[4][11]
        p_cl_cdfi = report_detail[4][12]
        p_cl_cal = report_detail[4][13]
        p_cl_echo_strong = report_detail[4][14]
        p_cl_sound = report_detail[4][15]
        p_cl_halo = report_detail[4][16]
        p_cl_supplement = report_detail[4][17]
        p_ct_position = report_detail[5][1]
        p_ct_type = report_detail[5][2]
        p_ct_num = report_detail[5][3]
        p_ct_size = report_detail[5][4]
        p_ct_grow = report_detail[5][5]
        p_ct_shape = report_detail[5][6]
        p_ct_edge = report_detail[5][7]
        p_ct_boundary = report_detail[5][8]
        p_ct_echo_inside = report_detail[5][9]
        p_ct_structure = report_detail[5][10]
        p_ct_echo_back = report_detail[5][11]
        p_ct_cdfi = report_detail[5][12]
        p_ct_cal = report_detail[5][13]
        p_ct_echo_strong = report_detail[5][14]
        p_ct_sound = report_detail[5][15]
        p_ct_halo = report_detail[5][16]
        p_ct_supplement = report_detail[5][17]

        tempDic = {'p_name': p_name, 'p_sex': p_sex, 'p_age': p_age, 'p_id': p_id, 'p_department': p_department,
                   'p_clinic': p_clinic, 'p_check_num': p_check_num, 'p_check_item': p_check_item,
                   'p_machine': p_machine, 'p_thickness_size': p_thickness_size, 'review_physician': review_physician,
                   'check_date': check_date, 'p_r_fb': p_r_fb, 'p_r_lr': p_r_lr, 'p_r_shape': p_r_shape,
                   'p_r_echo': p_r_echo, 'p_r_echo_d': p_r_echo_d, 'p_r_edge': p_r_edge, 'p_r_surface': p_r_surface,
                   'p_r_envelope': p_r_envelope, 'p_r_cdfi': p_r_cdfi, 'p_l_fb': p_l_fb, 'p_l_lr': p_l_lr, 'p_l_shape': p_l_shape,
                   'p_l_echo': p_l_echo, 'p_l_echo_d': p_l_echo_d, 'p_l_edge': p_l_edge, 'p_l_surface': p_l_surface,
                   'p_l_envelope': p_l_envelope, 'p_l_cdfi': p_l_cdfi, 'p_cr_position': p_cr_position,
                   'p_cr_type': p_cr_type, 'p_cr_num': p_cr_num, 'p_cr_size': p_cr_size, 'p_cr_grow': p_cr_grow,
                   'p_cr_shape': p_cr_shape, 'p_cr_edge': p_cr_edge, 'p_cr_boundary': p_cr_boundary,
                   'p_cr_echo_inside': p_cr_echo_inside, 'p_cr_structure': p_cr_structure, 'p_cr_echo_back':p_cr_echo_back,
                   'p_cr_cdfi': p_cr_cdfi, 'p_cr_cal': p_cr_cal, 'p_cr_echo_strong': p_cr_echo_strong,
                   'p_cr_sound': p_cr_sound, 'p_cr_halo': p_cr_halo, 'p_cr_supplement': p_cr_supplement, 'p_cl_position': p_cl_position,
                   'p_cl_type': p_cl_type, 'p_cl_num': p_cl_num, 'p_cl_size': p_cl_size, 'p_cl_grow': p_cl_grow,
                   'p_cl_shape': p_cl_shape, 'p_cl_edge': p_cl_edge, 'p_cl_boundary': p_cl_boundary,
                   'p_cl_echo_inside': p_cl_echo_inside, 'p_cl_structure': p_cl_structure, 'p_cl_echo_back':p_cl_echo_back,
                   'p_cl_cdfi': p_cl_cdfi, 'p_cl_cal': p_cl_cal, 'p_cl_echo_strong': p_cl_echo_strong,
                   'p_cl_sound': p_cl_sound, 'p_cl_halo': p_cl_halo, 'p_cl_supplement': p_cl_supplement, 'p_ct_position': p_ct_position,
                   'p_ct_type': p_ct_type, 'p_ct_num': p_ct_num, 'p_ct_size': p_ct_size, 'p_ct_grow': p_ct_grow,
                   'p_ct_shape': p_ct_shape, 'p_ct_edge': p_ct_edge, 'p_ct_boundary': p_ct_boundary,
                   'p_ct_echo_inside': p_ct_echo_inside, 'p_ct_structure': p_ct_structure, 'p_ct_echo_back':p_ct_echo_back,
                   'p_ct_cdfi': p_ct_cdfi, 'p_ct_cal': p_ct_cal, 'p_ct_echo_strong': p_ct_echo_strong,
                   'p_ct_sound': p_ct_sound, 'p_ct_halo': p_ct_halo, 'p_ct_supplement': p_ct_supplement}
        p_report_name = p_name + '_' + p_check_num + '_' + check_date
        report_ass = '/static/pdf/'+p_report_name+'.pdf'
        tempReportInfo = {'id': p_id, 'name': p_name, 'check': p_check_item, 'date': check_date, 'report': report_ass}
        # inputReportList.append(tempReportInfo)
        pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        f = open(pwd + "/mysite/static/pdf/report_list.txt", 'a+')
        write_str = '\n{' + "\"id\": \"" + p_check_num + "\", \"name\": \"" + p_name + "\", \"check\": \"" + p_check_item + "\", \"date\": \"" + check_date + "\", \"report\": \"" + report_ass + "\"}"
        print(write_str)
        f.write(write_str)
        f.close()
        data = dict()
        print('1')
        template = get_template('pdf.html')
        html = template.render(tempDic)
        # html = template.render(data)
        url = 'http://localhost:6000/pdf/'
        str_file_name = p_name+"_"+p_check_num+"_"+check_date
        filename = "static\\pdf\\" + str_file_name + ".pdf"
        confg = pdfkit.configuration(wkhtmltopdf=r'D:\wkhtmltopdf\bin\wkhtmltopdf.exe')
        css = [r"E:\workspace_django\mysite\static\css\test.css", r"E:\workspace_django\mysite\static\css\styles.css"]
        pdf = pdfkit.from_string(html, filename, css=css, configuration=confg)
        # pdf = pdfkit.from_url(url, filename, configuration=confg)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        f = open(pwd + "/mysite/static/check_num.txt", 'w')
        p_check_num = int(p_check_num) + 1
        f.write(str(p_check_num))
        return redirect('/pdf', {'p_name': p_name , 'p_sex': p_sex, 'p_age': p_age, 'p_id': p_id})
        # pwd = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # file = pwd+"/mysite/templates/test.html"
        # print(file)
        # pdf_dict = pwd+"/mysite/static/pdf/"
        # print(pdf_dict)
        # url = r'http://localhost:6000/test/'
        # confg = pdfkit.configuration(wkhtmltopdf=r'D:\wkhtmltopdf\bin\wkhtmltopdf.exe')
        # # pdfkit.from_url(url, dict+'temp.pdf', configuration=confg)
        # pdfkit.from_file(file, pdf_dict+'temp.pdf', configuration=confg)
        # result = 'success'
        # print('success')
        # return render(request, 'test.html')
    return JsonResponse(result)

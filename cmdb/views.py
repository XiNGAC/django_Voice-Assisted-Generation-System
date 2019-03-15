from django.shortcuts import render, redirect

from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import os
from django.contrib import auth
from django.contrib.auth.models import User
from django.forms import fields
from django import forms
from cmdb.models import ReportDetail
import json
from aip import AipSpeech
import codecs
import hashlib
import base64
import urllib
from urllib import parse
import time
import urllib.request
import requests

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
    return render(request, "test.html",)


def forms(request):
    return render(request, "forms.html",)


def a_report_input(request):
    return render(request, "a_report_input.html",)


def a_recognition(request):
    return render(request, "a_recognition.html",)


def a_recognition_submit(request):
    if request.method == "POST":
        input_str = request.POST.get("report_input")
        print(input_str)
    print('helloworld')
    result_str = 'recognition submit as '+input_str
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
            print(register_add)
            message = "注册成功"
            if register_add == False:
                print('3')
                return render(request, 'share1.html', {'registAdd': register_add, 'username': username})
    else:
        uf = UserForm()
        print('4')
    return HttpResponse(message)
    # return render(request, 'register.html')


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
    return render(request, "a_report_input.html")


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
    with connection.cursor() as c:
        c.execute("select * from report_detail where report_id = '1'")
        report_detail = c.fetchall()
        print(report_detail)
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
        resultdata = jsondata['data']['block'][0]['line'][0]['word'][0]['content']
        print(resultdata)
        return JsonResponse(resultdata, safe=False);


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
        size_right_UL =temp_json['size_right_UL']
        size_right_LR = temp_json['size_right_LR']
        size_right_FB =temp_json['size_right_FB']
        size_left_UL = temp_json['size_left_UL']
        size_left_LR = temp_json['size_left_LR']
        size_left_FB = temp_json['size_left_FB']
        size_thickness = temp_json['size_thickness']
        size_normal = temp_json['size_normal']
        substantial_echo =temp_json['substantial_echo']
        lump_echo = temp_json['lump_echo']
        blood_flow_distribution = temp_json['blood_flow_distribution']
        blood_flow_spectrum = temp_json['blood_flow_spectrum']
        left_PSV = temp_json['left_PSV']
        left_EDV = temp_json['left_EDV']
        right_PSV = temp_json['right_PSV']
        right_EDV =temp_json['right_EDV']
        diagnosis = temp_json['diagnosis']
        review_physician = temp_json['review_physician']
        check_date = temp_json['check_date']
        print(patient_id, department_name, check_item, machine_number, size_left_FB, size_thickness, left_EDV)
        create = ReportDetail.objects.create(patient_id=patient_id, department_name=department_name,
                                             check_item=check_item, machine_number=machine_number,
                                             size_right_ul=size_right_UL, size_right_lr=size_right_LR,
                                             size_right_fb=size_right_FB, size_left_ul=size_left_UL,
                                             size_left_lr=size_left_LR, size_left_fb=size_left_FB,
                                             size_thickness=size_thickness, size_normal=size_normal,
                                             substantial_echo=substantial_echo, lump_echo=lump_echo,
                                             blood_flow_distribution=blood_flow_distribution,
                                             blood_flow_spectrum=blood_flow_spectrum, left_psv=left_PSV,
                                             left_edv=left_EDV, right_psv=right_PSV, right_edv=right_EDV,
                                             diagnosis=diagnosis, review_physician=review_physician,
                                             check_date=check_date)
        print(type(create), create)
        return JsonResponse(temp_json, safe=False)
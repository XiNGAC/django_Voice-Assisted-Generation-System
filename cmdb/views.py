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


def temp(request):
    return render(request, "temp.html",)


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
            return redirect("/temp", {'user': re})
        else:
            return render(request, 'login.html', {'login_error': '用户名或密码错误'})
    return render(request, "login.html",)


def logout(request):
    auth.logout(request)
    return render(request, "temp.html")


def xx(request):
    return render(request, "to_use_py_test.html",)


def audio_test(request):
    return render(request, "audio_test.html",)


@csrf_exempt
def ajax_patient(request):
    with connection.cursor() as c:
        c.execute("select patient_name,patient_sex, patient_age from patient")
        patients = c.fetchall()
        print(patients)
    return JsonResponse(patients, safe=False)


def ajax_patient_info(request):
    with connection.cursor() as c:
        c.execute("select patient_name,patient_sex,patient_age from patient where patient_name=%s" [p_name])
        patient_info = c.fetchall()
    return JsonResponse(patient_info, safe=False)


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
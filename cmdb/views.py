from django.shortcuts import render

from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import os
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


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("hello world")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
    return render(request, "index.html",)


def sousuo(request):
    return render(request, "index.html",)


def forms(request):
    return render(request, "forms.html",)


def temp(request):
    return render(request, "temp.html",)


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
            with open(pwd+"/mysite/static/radio/%s" % file.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in file.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, 'upload.html')
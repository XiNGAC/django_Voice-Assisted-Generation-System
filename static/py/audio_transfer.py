
# -*- coding:utf-8 -*-
from aip import AipSpeech
import codecs
import wave
import threading
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import time
import json

APP_ID = '14937377'
API_KEY = 'HrgplyNyIMrZwawxCqLit04D'
SECRET_KEY = 'xRsQe5AIzHq7ALmyl4rZmG7OeaSsEBHS'

filex = "E:/workspace_django/mysite/static/test.wav"


fileName = None
allowRecording = False


time_count = -1;





# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def dealwav():
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 识别本地文件
    an = client.asr(get_file_content(filex), 'wav', 16000, {'dev_pid': 1536,})
    '''json_dict = json.loads(an)
    result = json_dict['result']'''
    f = codecs.open('E:/workspace_django/mysite/static/test.txt', 'w', encoding='utf-8')
    str = ''.join(an['result'])
    f.write(str)
    f.close





dealwav()


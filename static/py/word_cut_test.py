import jieba
import re
import operator
import pymysql

db = pymysql.connect("localhost", "root", "123456", "sql_db")
cursor = db.cursor()
sql_delete = "DELETE FROM REPORT_DETAIL WHERE REPORT_ID = '1'"
try:
    cursor.execute(sql_delete)
    print("commit")
    db.commit()
except:
    db.rollback()
    print("rollback")

f = open('E:/workspace_django/mysite/static/test.txt', 'rb')
f_String = f.read()
f_s = f_String.decode('utf-8')
print(f_s)

string = "甲状腺大小正常，左叶大小29*19*20mm，右叶大小25*14mm，包膜完整，峡部厚度20mm，5mm，右叶腺体内可见0.2*0.3厘米的低回声结节，边界清，内部回声尚均，cdfi未见异常血流信号。"
seg_list = jieba.cut(string, cut_all=False)
# print("Full Mode:", ' '.join(seg_list))

size = re.findall(".*甲状腺(?:大小|形态)(.*?)(?:，|。).*", string)
print(operator.eq(size, ["正常"]))
size_normal = ''.join(size)
# print(size_normal)

xbhd = re.findall(".*峡部厚度(.*?)mm.*", string)
str_xbhd = ''.join(xbhd)
# print(str_xbhd + 'mm')

baomo = re.findall(".*包膜(.*?)(?:，|。).*", string)
str_baomo = ''.join(baomo)
# print(str_baomo)

left_size = re.findall(".*左叶大小(.*?)(?:，|。).*", string)
str_left_size = ''.join(left_size)
# print(str_left_size)
left_size_123 = re.findall("\d+", str_left_size)
left_size_1 = int(left_size_123[0])
if len(left_size_123) == 1:
    left_size_2 = 0
    left_size_3 = 0
else:
    left_size_2 = int(left_size_123[1])
    if len(left_size_123) == 2:
        left_size_3 = 0
    else:
        left_size_3 = int(left_size_123[2])
# print(left_size_1)

right_size = re.findall(".*右叶大小(.*?)(?:，|。).*", string)
str_right_size = ''.join(right_size)
# print(str_right_size)
right_size_123 = re.findall("\d+", str_right_size)
right_size_1 = int(right_size_123[0])
if len(right_size_123) == 1:
    right_size_2 = 0
    right_size_3 = 0
else:
    right_size_2 = int(right_size_123[1])
    if len(right_size_123) == 2:
        right_size_3 = 0
    else:
        right_size_3 = int(right_size_123[2])
# print(right_size_1)
# print(right_size_2)
# print(right_size_3)

thickness = re.findall(".*峡部(.*?)mm(?:，|。).*", string)
temp = ''.join(thickness)
str_thickness = ''.join(re.findall("\d+", temp))
if len(str_thickness) == 0: str_thickness = '0'
str_thickness = int(str_thickness)
# print(str_thickness)


substantial_echo = re.findall(".*(?:内部|实质)回声(.*?)(?:，|。).*", string)
str_substantial_echo = ''.join(substantial_echo)
# print(str_substantial_echo)

lump_echo = re.findall(".*，(.*?)(?:肿块回声|回声结节).*", string)
str_lump_echo = ''.join(lump_echo)
# print(str_lump_echo)

blood_flow_d = re.findall(".*血流分布(.*?)(?:，|。).*", string)
str_blood_flow_d = ''.join(blood_flow_d)

blood_flow_s = re.findall(".*血流频率(.*?)(?:，|。).*", string)
str_blood_flow_s = ''.join(blood_flow_s)

left_blood = re.findall(".*左侧动脉(.*?)(?:，|。).*", string)
str_left_blood = ''.join(left_blood)
left_PSV = re.findall(".*PSV=(.*?).*", str_left_blood)
str_left_PSV = ''.join(left_PSV)
if len(str_left_PSV) == 0: str_left_PSV = '0'
str_left_PSV = int(str_left_PSV)
left_EDV = re.findall(".*EDV=(.*?).*", str_left_blood)
str_left_EDV = ''.join(left_EDV)
if len(str_left_EDV) == 0: str_left_EDV = '0'
str_left_EDV = int(str_left_EDV)

right_blood = re.findall(".*右侧动脉(.*?)(?:，|。).*", string)
str_right_blood = ''.join(right_blood)
right_PSV = re.findall(".*PSV=(.*?).*", str_right_blood)
str_right_PSV = ''.join(right_PSV)
if len(str_right_PSV) == 0: str_right_PSV = '0'
str_right_PSV = int(str_right_PSV)
right_EDV = re.findall(".*EDV=(.*?).*", str_right_blood)
str_right_EDV = ''.join(right_EDV)
if len(str_right_EDV) == 0: str_right_EDV = '0'
str_right_EDV = int(str_right_EDV)

sql_insert = "INSERT INTO REPORT_DETAIL (report_id, patient_id, department_name,check_item,\
            machine_number, size_right_UL, size_right_LR, size_right_FB, size_left_UL, \
            size_left_LR, size_left_FB, size_thickness, size_normal,  substantial_echo, \
            lump_echo, blood_flow_distribution, blood_flow_spectrum, left_PSV, left_EDV, \
            right_PSV, right_EDV) VALUES ('%s','%s','%s','%s','%s', '%d', '%d','%d','%d','%d',\
            '%d','%d','%s','%s', '%s', '%s','%s','%d','%d','%d','%d')" % ('1', 'temp', \
                                                                          '门诊', '超声', '1', right_size_1, right_size_2,
                                                                          right_size_3, left_size_1, \
                                                                          left_size_2, left_size_3, int(str_thickness), \
                                                                          size_normal, str_substantial_echo,
                                                                          str_lump_echo, str_blood_flow_d, \
                                                                          str_blood_flow_s, int(str_left_PSV),
                                                                          int(str_left_EDV), int(str_right_PSV), \
                                                                          int(str_right_EDV))

try:
    cursor.execute(sql_insert)
    db.commit()
    # print("good")
except Exception:
    db.rollback()
    # print("wtf")
db.close()
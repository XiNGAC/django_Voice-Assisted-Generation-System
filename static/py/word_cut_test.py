import jieba
import re
import operator
string = "甲状腺大小正常，左叶大小29*19*20mm，右叶大小25*14mm，包膜完整，峡部厚度20mm，5mm，右叶腺体内可见0.2*0.3厘米的低回声结节，边界清，内部回声尚均，cdfi未见异常血流信号。"
seg_list = jieba.cut(string, cut_all = False)
print("Full Mode:", ' '.join(seg_list))

size = re.findall(".*甲状腺(?:大小|形态)(.*?)(?:，|。).*", string)
print(operator.eq(size, ["正常"]))
size_normal = ''.join(size)
print(size_normal)

xbhd = re.findall(".*峡部厚度(.*?)mm.*", string)
str_xbhd = ''.join(xbhd)
print(str_xbhd + 'mm')

baomo = re.findall(".*包膜(.*?)(?:，|。).*", string)
str_baomo = ''.join(baomo)
print(str_baomo)

left_size = re.findall(".*左叶大小(.*?)(?:，|。).*", string)
str_left_size = ''.join(left_size)
print(str_left_size)
left_size_123 = re.findall("\d+",str_left_size)
left_size_1 = left_size_123[0]
if len(left_size_123) == 1:
    left_size_2 = 0
    left_size_3 = 0
else:
    left_size_2 = left_size_123[1]
    if len(left_size_123) == 2:
        left_size_3 = 0
    else:
        left_size_3 = left_size_123[2]
# print(left_size_1)

right_size = re.findall(".*右叶大小(.*?)(?:，|。).*", string)
str_right_size = ''.join(right_size)
print(str_right_size)
right_size_123 = re.findall("\d+", str_right_size)
right_size_1 = right_size_123[0]
if len(right_size_123) == 1:
    right_size_2 = 0
    right_size_3 = 0
else:
    right_size_2 = right_size_123[1]
    if len(right_size_123) == 2:
        right_size_3 = 0
    else:
        right_size_3 = right_size_123[2]
print(right_size_1)
print(right_size_2)
print(right_size_3)

thickness = re.findall(".*峡部(.*?)mm(?:，|。).*", string)
temp = ''.join(thickness)
str_thickness = ''.join(re.findall("\d+", temp))
print(str_thickness)


substantial_echo = re.findall(".*(?:内部|实质)回声(.*?)(?:，|。).*", string)
str_substantial_echo = ''.join(substantial_echo)
print(str_substantial_echo)

lump_echo = re.findall(".*，(.*?)(?:肿块回声|回声结节).*", string)
str_lump_echo = ''.join(lump_echo)
print(str_lump_echo)

blood_flow_d = re.findall(".*血流分布(.*?)(?:，|。).*", string)
str_blood_flow_d = ''.join(blood_flow_d)

blood_flow_s = re.findall(".*血流频率(.*?)(?:，|。).*", string)
str_blood_flow_s = ''.join(blood_flow_s)

left_blood = re.findall(".*左侧动脉(.*?)(?:，|。).*", string)
str_left_blood = ''.join(left_blood)
left_PSV = re.findall(".*PSV=(.*?).*", str_left_blood)
left_EDV = re.findall(".*EDV=(.*?).*", str_left_blood)

right_blood = re.findall(".*右侧动脉(.*?)(?:，|。).*", string)
str_right_blood = ''.join(right_blood)
right_PSV = re.findall(".*PSV=(.*?).*", str_right_blood)
right_EDV = re.findall(".*EDV=(.*?).*", str_right_blood)
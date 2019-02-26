import jieba
import re
import operator
string = "甲状腺大小正常，包膜完整，峡部厚度20mm，右叶腺体内可见0.2*0.3厘米的低回声结节，边界清，内部回声尚均，cdfi未见异常血流信号"
seg_list = jieba.cut(string, cut_all = False)
print ("Full Mode:", ' '.join(seg_list))

size =  re.findall(".*大小(.*?)，.*",string)
print(operator.eq(size,["正常"]))
str_size = ''.join(size)
print (str_size)

xbhd = re.findall(".*峡部厚度(.*?)mm.*",string)
str_xbhd = ''.join(xbhd)
print (str_xbhd + 'mm')

baomo = re.findall(".*包膜(.*?)，.*",string)
str_baomo = ''.join(baomo)
print(str_baomo)


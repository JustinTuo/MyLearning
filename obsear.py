# _*_coding:utf-8 _*_
# import re
#
# line = "Cats are smarter than dogs"
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
#     print "searchObj.group(1) : ", searchObj.group(1)
#     print "searchObj.group(2) : ", searchObj.group(2)
# else:
#     print "Nothing found!!"
'''import re

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"
'''
import re
def psrea(str):
    "Python检索和替换的正则表达式"
    # str = raw_input(str)
    print psrea.__doc__
    print str
    return
# r = psrea("ninhao")
phone = "2004-959-559" #这是一个国外电话号码
#删除字符串中的python注释
num = re.sub(r'#.*$',"",phone)
print "电话号码是：",num
#删除非数字
# num = re.sub(r'\D',"",phone)
# print "电话号码是：",num
num1 = re.sub('\D',"",phone,count=0,flags=0)
print num1
num2 = re.match(r'\d',phone)
print num2

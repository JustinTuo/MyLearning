# _*_ coding:utf-8 _*_
import sys; x='runoob'; sys.stdout.write(x+'\n'); # 这是一个注释
x='a'
y='b'
print x,# 不换行输出
print y,#不换行输出
print x #换行输出
print y #换行输出
print x,y
# raw_input("\n\nPress the enter key to exit.") #等待用户输入回车键就退出:

#多个语句构成代码组
'''if expression :
    suite
elif expression :
    suite
else :
    suite
'''
# Python 命令行参数
import sys
print sys.argv

#! /usr/bin/env python
import sys
print sys.argv
#Python变量赋值
counter=100 #赋值整型变量
miles=1000.0 #赋值浮点型变量
name='John' #赋值字符串型变量
print counter,
print miles,
print name
#多个变量赋值
a=b=c=1 #a,b,c被分配到相同的内存空间上
d,e,f=1,2,'John'
print a,b,c
print d,e,f

var1=1
var2=25
del var1
print var1
print var2



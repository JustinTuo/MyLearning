# /Users/tzhangw/AppData/Local/Programs/Python
# _*_ coding:utf-8 _*_
# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用函数
printme("我抱你带给浦东阿道夫");
printme("再次调用同一函数");

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;
print"两个数相加后的结果为：", sum(2345, 8090.3)

money = 2000
def addmoney():
    global money
    money = money +1
print money
addmoney()
print money
reload(re)
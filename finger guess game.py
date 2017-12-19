# _*_ coding=utf-8 _*_
import random
while 1:
    s = int(random.randint(1,3))
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪刀"
    elif s == 3:
        ind = "布"
    m = raw_input('请输入 石头、剪刀、布，输入"end"结束游戏：')
    blist = ['石头','剪刀','布']
    if (m not in blist) and (m != 'end'):
        print "输入错误，请重新输入"
    elif (m not in blist) and (m == 'end'):
        print "\n游戏退出中......"
        break
    elif m == ind:
        print "电脑出了："+ ind + ",平局"
    elif (m =='石头' and ind =='剪刀') or (m =='剪刀' and ind == '布') or (m == '布' and ind == '石头'):
        print "电脑出了："+ ind + "，恭喜您，您赢了！"
    elif (ind =='石头' and m =='剪刀') or (ind =='剪刀' and m == '布') or (ind == '布' and m == '石头'):
        print "电脑出了："+ ind + "，很遗憾，您输了！"



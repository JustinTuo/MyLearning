# _*_ coding=utf-8 _*_
dictinary ={}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
    flag = raw_input("添加或者查找单词？（a/c)")
    if flag == 'a':    #开启
        word = raw_input("请输入单词（key):")
        defintion = raw_input("请输入定义的值（Value):")
        dictinary[str(word)] = str(defintion) #添加字典
        print "添加成功"
        pape = raw_input("您是否需要查找字典？（a/0）") #read
        if pape == "a":
            print dictinary
        else:
            continue
    elif flag =="c":
        check_word = raw_input("要查找的单词：")  #检索
        for key in sorted(dictinary.keys()):
            if str(check_word)==key:
                print "该单词存在！",key,dictinary[key]
                break
            else:
                off = "b"
            if off=="b":
                print "抱歉，该值不存在！"
    else:
        print "error type"
        break






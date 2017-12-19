# _*_ coding=utf-8 _*_
i=1
while i<100:
    i +=1
    if i%2 >0:
        continue
    print i

i=1
while i<10:
    i+=1
    if i%2>0:
        continue
    print i

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number  :")
    var=var+1
    print "You entered: ", num

print "Good bye!"
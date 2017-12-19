# _*_ coding:utf-8 _*_
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
#
# t = Test()
# t.prt()
# print Test.__dict__
# class test1:
#     "这是一个测试类文档字符串"
#     def prt(self):
#         print(self.__doc__)
# test1().prt()
# class student:
#     stucount = 10
#     def __init__(self1,name,studentno):
#         self1.name = name
#         self1.studentno = studentno
#         student.stucount += 1
#     def displaycount(self1):
#         print "Total student %d" % student.stucount
#     def displaystudent(self1):
#         print "Name:",self1.name,",studentno:",self1.studentno
# "创建student的第一个对象"
# stu1 = student("Liu Wei",20171201)
# stu2 = student("Li San",20171202)
# stu1.displaystudent()
# stu2.displaystudent()
# print "Total student %d" % student.stucount
#
# setattr(student,'age',23)
# print student.__dict__

class point:
    def __init__(self2,x = 0, y = 0):
        self2.x = x
        self2.y = y
    def __del__(self2):
        class_name = self2.__class__.__name__
        print class_name,"销毁"
pt1 = point()
print pt1
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3)
del pt1
del pt2
del pt3


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2
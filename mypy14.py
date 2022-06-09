#测试方法的重写

class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def say_age(self):
        print("年龄是:{}".format(self.__age))

    def say_nanme(self):
        print("名字是：{}".format(self.name))


class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)    #必须显示的调用父类初始化方法，不然解释器不会取调用
        self.score=score

    def say_nanme(self):
        '''重写了父类的方法'''
        print("报告，我的名字是：{}".format(self.name))


s1=Student("czx",3,90)
s1.say_age()
s1.say_nanme()
'''
class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(C.mro())
'''
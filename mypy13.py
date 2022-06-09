#测试继承的基本使用

class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age  #私有属性同样也会继承


    def say_age(self):
        print("年龄是多少呢？")

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)    #必须显示的调用父类初始化方法，不然解释器不会取调用
        self.score=score



#Student类继承-->Person类继承-->object类
print(Student.mro())

s1=Student("cjs",32,90)
s1.say_age()
print(s1.name)
print(s1._Person__age)     #父类私有属性子类调用必须使用方法调用

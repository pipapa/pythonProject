#测试super()，获得父类的定义，而不是父类的对象

class A:
    def say(self):
        print("A:",self)
    def __str__(self):
        return "描述"


class B(A):
    def say(self):
        #A.say(self)             #直接调用A的方法
        super(B,self).say()       #可以使用super()方法调用父类的定义
        print("B:",self)

b=B()
b.say()

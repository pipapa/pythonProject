#多态
class Man:
    def eat(self):
        print("各国吃饭方法")

class Chinese(Man):
    def eat(self):
        print("中国人使用筷子")

class Amircan(Man):
    def eat(self):
        print("美国人使用筷子")

class Indian(Man):
    def eat(self):
        print("印度人使用筷子")

def toeat(m):
    if isinstance(m,Man):        #判断对象是不是指定类型
        m.eat()                  #多态。一个方法调用，根据对象不同调用不同的方法！
    else:
        print("不能吃饭")

ch=Chinese()
us=Amircan()
ind=Indian()

toeat(ch)
toeat(us)
toeat(ind)
#测试特殊属性

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D:
    pass
class E(A,D):
    pass
a1=A()
print(a1.__dict__)
print(a1.__class__)
print(E.__bases__)
print(E.__base__)
print(E.__mro__)
print(A.__subclasses__())

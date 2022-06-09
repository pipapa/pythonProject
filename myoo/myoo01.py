#测试运算符的重载
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "{}的年龄是{}".format(self.name,self.age)

    def __add__(self, other):
        if isinstance(other,Person):
            return self.name+other.name
        else:
            return "不是同类不能相加"
    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类不能乘"

p1=Person("cjs",32)
p2=Person("czx",3)
x=p1+p2

print(p2)
print(p1.name+p2.name)
print(x)
print(x*3)



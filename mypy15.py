#测试查看对象属性

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "测试对象描述"

    def say_age(self):
        print(self.name,"的年龄是：",self.age)

obj=object()
print(dir(obj))

p1=Person("cjs",32)
print(dir(p1))
print(p1)
print(Person)

# @property 装饰器使用

class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property             #装饰器将实例方法变为实例属性
    def salarys(self):
        return self.__salary
    @salarys.setter
    def salarys(self,salary):
        if 1000 < salary < 20000:
            self.__salary = salary
        else:
            print("请输入1000-20000的薪资")

'''
    @property
    def get_salary(self):
        return self.salary

    def set_salary(self,salary):
        if 1000<salary<20000:
            self.salary=salary
        else:
            print("请输入1000-20000的薪资")
'''


e1=Employee("陈建苏",4200)
print(e1.salarys)
e1.salarys=10000
print(e1.salarys)
#e1.salarys=5000       #可以当作属性来调用，但不可以设置
# e1.set_salary(10000)
# print(e1.get_salary)





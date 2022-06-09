#@property装饰器测试

class Employee:

    @property
    def salary(self):
        return 10000

e1=Employee()
print(e1.salary)         #打印10000
print(type(e1.salary))   #打印<class 'int'>
#e1.salary()             #TypeError: 'int' object is not callable
#e1.salary=20000          #@property 修饰的属性，如果没有家setter方法，则为只读属性。此处修改报错：AttributeError: can't set attribute 'salary'
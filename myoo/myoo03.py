#测试工厂模式

class CarFactory:
    def create_car(self,brand):
        if brand=="奔驰":
            return Benz()
        elif brand=="宝马":
            return Bmw()
        elif brand=="比亚迪":
            return Byd()
        else:
            print("不能创建")

class Benz:
    def models(self,x):
        if x=="A系":
            return "A150"
        elif x=="C系":
            return "C300"
        else:
            print("不能制造")




class Bmw:
    pass

class Byd:
    pass

factory=CarFactory()
c1=factory.create_car("奔驰").models("A系")
c2=factory.create_car("宝马")
c3=factory.create_car("比亚迪")

print(c1)





#测试对象的浅拷贝和深拷贝
import copy

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen

class Cpu:
    def calculate(self):
        print("cpu算力惊人")
        print("cpu对象：",self)
class Screen:
    def show(self):
        print("屏幕亮度惊人")
        print("screen对象：",self)


#测试变量赋值
c1=Cpu()
c2=c1
print(c1)
print(c2)

#测试浅赋值
print("测试浅复制")
s1=Screen()
mp1=MobilePhone(c1,s1)
mp2=copy.copy(mp1)
print(mp1,mp1.cpu,mp1.screen)
print(mp2,mp2.cpu,mp2.screen)

#测试深赋值
print("测试深复制")
mp3=copy.deepcopy(mp1)
print(mp1,mp1.cpu,mp1.screen)
print(mp3,mp3.cpu,mp3.screen)


mp1.cpu.calculate()
mp1.screen.show()






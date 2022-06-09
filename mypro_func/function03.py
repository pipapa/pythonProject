#测试全局变量、局部变量

a=3                         #全局变量
def test01():
    b=100                   #局部变量
    print(b)
    global a               #如果要在函数内改变全局变量的值，增加global关键字声明
    print(a)               #打印全局变量的值
    a=150
    print(locals())        #打印输出的局部变量
    print(globals())       #打印输出的全局变量

test01()

#测试局部变量和全局变量效率
import math
import time

def test02():
    start = time.time()
    for i in range(10000000):
        math.sqrt(81)           #全局变量
    end=time.time()
    print("耗时：{}".format(end-start))

def test03():
    b=math.sqrt                 #局部变量
    start = time.time()
    for i in range(10000000):
        b(81)
    end=time.time()
    print("耗时：{}".format(end-start))

test02()
test03()






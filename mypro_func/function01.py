#测试函数的定义和调用

def  test01():
    print("*"*10)
    print("@"*10)

test01()
test01()
test01()
for i in range(10):
    test01()

def test02(a,b):
    '''比较a和b两个值'''
    if a>b:
        print(a,"较大值")
    else:
        print(b,"较小值")

test02(10,15)
test02(20,11)
test02(11,11)

#测试注释字符串

def test03(x):
    '''根据传入的x，打印多个星号'''
    print("*"*x)

test03(20)

help(test03.__doc__)

print("**********")


#测试返回值（return）的基本用法

def test04(a,b):

    return a-b         #return 两个作用 1。返回值；2。结束函数的执行

test04(11,12)


print(test04(15,11))


def  test05(x):
    print("*"*x)
    return ("@"*3)

print(test05(30))

def test06(a,b):
    return (a+b)/2

print(test06(10,20))

def test07(a,b):
    return [(a+b),(a-b),(a*b),int(a/b)]         #返回值为列表

print(test07(20,10))


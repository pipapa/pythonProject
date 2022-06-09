#测试nonlocal gaobal 关键字

b=100
def outer():
    a=10
    def inner():
        nonlocal a      #声明外部函数的局部变量
        print("inner:",a)
        a=20
    global b          #声明全局变量
    b=1000

    inner()
    print("outer:",a)

outer()
print("b:",b)


#测试 LEGB

# str2="chenzixuan"

def outer():
    # str2="baihonglan"
    def inner():
        # str2="chenjiansu"
        print(str2)
    inner()
outer()




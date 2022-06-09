#测试递归函数

def factorial(n):                #factorial(阶梯，递归乘)
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

for i in range(1,6):
    print(i,"!=",factorial(i))



def test01(n):                     #增加参数
    print("test01",n)
    if n==0:                      #增加条件
        print("it's over")
    else:
        test01(n-1)             #增加递归关系

test01(4)
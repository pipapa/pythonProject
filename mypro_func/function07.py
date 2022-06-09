#测试lambda表达式使用

f=lambda a,b,c,d:a*b*c*d

def test01(a,b,c,d):
    print("########")
    return a*b*c*d

print(f)

print(f(2,3,4,5))

g=[lambda a:a*2,lambda b:b*3]

print(g[0](6))

h=[test01,test01]    #函数也是对象
print(h[0](3,4,5,6))


#测试 eval() 函数：

s="print('abcdef')"

eval(s)

a=10
b=20
c=eval("a+b")
print(c)

dict1=dict(a=100,b=200)

d=eval("a+b")

print(d)

d=eval("a+b",dict1)     #后面加参数就是可到的相应的结果

print(d)
#测试参数的传递
#传递可变对象

b=[10,20]
print(id(b))
print(b)
print("****************")

def test01(m):
    print(id(m))
    m.append(30)
    print(id(m))

test01(b)
print(b)

print("*********************")

#传递不可变对象
a=100

def test02(n):
    print(id(n))        #传递进来的是a对象的地址
    print(a)
    n=n+200             #由于a是不可变对象，因此创建新的对象n
    print(id(n))        #n已经是新的对象
    print(n)
    print(type(n))


test02(a)
print(id(a))
print(a)
test02((0.1))

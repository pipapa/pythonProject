# 参数的几种类型测试

#位置参数测试

def test01(a,b,c):
    print(a,b,c)

test01(3,4,5)
test01(6,7,8)             #会报错，位置参数不匹配，形参有3个，实参只有2个。

#默认值参数测试

def test02(a,b,c=10,d=20):          #默认值参数必须位于普通参数位置后面
    print(a,b,c,d)

test02(8,9)
test02(8,9,19)
test02(8,9,19,29)


#命名参数测试

def test03(a,b,c):
    print(a,b,c,)

test03(c=20,a=18,b=5)            #命名参数，通过形参名称来匹配


#可变参数测试

def test04(a,b,*c):
    print(a,b,c)

def test05(a,b,**c):
    print(a,b,c)

def test06(a,b,*c,**d):
    print(a,b,c,d)

test04(5,6,7,8,9)

test05(5,6,name="chenjiansu",age=32)

test06(5,6,8,9,name="chenjiansu",age=32)

#强制命名参数测试

def test07(*a,b,c):
    print(a,b,c)

test07(3,b=4,c=5)          #会报错。由于a是可变参数，可将2，3，4全部收集。造成b和c没有赋值
test07(3,b=4,c=5)


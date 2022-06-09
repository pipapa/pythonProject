#测试前拷贝、深拷贝

import copy
def Copy():
    """测试浅拷贝"""
    a=[10,20,[5,6]]
    b=copy.copy(a)

    print("a:",a)
    print("b:",b)
    print("a:",id(a))
    print("b:",id(b))

    b.append(30)
    b[2].append(7)

    print("浅拷贝 copy")

    print("a:",a)
    print("b:",b)
    print("a:", id(a))
    print("b:", id(b))

Copy()
print("***********************")
def DeepCopy():
    """测试深拷贝"""
    a=[10,20,[5,6]]
    b=copy.deepcopy(a)

    print("a:",a)
    print("b:",b)
    print(id(a))
    print(id(b))

    b.append(30)
    b[2].append(7)

    print("深拷贝 deepcopy")

    print("a:",a)
    print("b:",b)

DeepCopy()

print("***********************")

#传递不可变对象时，不可变对象里包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生改变。

a=(10,20,[5,6])
print("a:",id(a))

def test01(m):
    print("m:",id(m))
    m[2][0]=888
    print(m)
    print("m:", id(m))

test01(a)
print(a)

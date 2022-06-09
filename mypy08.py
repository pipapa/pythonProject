#测试嵌套函数（内部函数）的定义

def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()

outer()


#打印中英文姓名


def printChineseName(name, familyName):
    print("{0} {1}".format(familyName, name))


def printEeglishName(name, familyName):
    print("{0} {1}".format(familyName, name))



def printName(isChinese,name,familyName):

    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"jiansu","chen")
printName(False,"mochael","jordan")


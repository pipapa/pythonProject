#练习选择结构嵌套

score=int(input("这里输入一个分数"))
if score<0 or score>100:
    print("输入错误，请重新输入一个0~100的分数")
else:
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("E")

print("**************************************************")

score=int(input("这里输入一个分数"))
degree="ABCDE"
num=0
if score<0 or score>100:
    print("请重新输入一个0～100之间的分数")
else:
    num=score//10
    if num<6:
        num=5
    print(degree[9-num])

print("*************************")

score=int(input("这里输入一个分数"))
great=""
degree="ABCDE"
num=0
if score<0 or score>100:
    score=int(input("输入错误，请重新输入一个0~100的分数"))
else:
    num=score//10
    if num<6:
        num=5
    print("score：{0},great：{1}".format(score,degree[9-num]))





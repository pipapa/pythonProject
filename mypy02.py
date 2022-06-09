#双分支机构

a=input("这里输入一个数字")
if int(a) <10:
    print("a小于3")
else:
    print("a大于等于10")

#使用三元运算符表达双分支结构

a=input("这里输入一个数字")

print("a小于10" if int(a)<10  else "a大于等于10")

#多分支选择结构

#方法1： 这里条件选择结构可以不按顺序
score=int(input("输入分数"))
grade=""
if score<60:
    grade="不及格"
if 60<=score<=79:
    grade="及格"
if 80<=score<=89:
    grade="良好"
if 90<=score<=100:
    grade="优秀"

#.format()字符串"分数是{0},等级是{1}"中{}格式化
print("分数是{0},等级是{1}".format(score,grade))


#测试多分支结构
# 方法2 ：这里必须按照逻辑顺序
score=int(input("这里输入分数"))
grade=""
if score<60:
    grade="不及格"
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
else:
    grade="优秀"

#.format()字符串"分数是{0},等级是{1}"中{}格式化
print("分数是{0},等级是{1}".format(score,grade))




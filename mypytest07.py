#测试zip()并行迭代
names=("陈大","王二","张三","李四")
ages=(30,31,32,33)
jobs=("公务员","医生","教师")

for a,b,c in zip(names,ages,jobs):
    print("{}--{}--{}".format(a,b,c))


for i in range(3):
    print("{}--{}--{}".format(names[i],ages[i],jobs[i]))

for i in range(3):
    print(names[i])
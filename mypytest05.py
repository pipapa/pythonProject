#测试 break
while True:
    a=input("当输入字符（Q或者q结束）")
    if a.upper()=="Q":
        print("循环结束")
        break
    else:
        print(a)

print("**********")

num=0
sum=0
salarys=[]
while True:
    a=input("输入员工薪资（按Q或者q结束）")
    if a.upper()=="Q":
        print("录入完成，退出")
        break #break 语句执行整个循环结束
    if float(a)<=0:
        continue
    num+=1
    salarys.append(float(a))
    sum+=float(a)

print("员工数量：{}".format(int(num)))
print("录入薪资:",salarys)
print("平均薪资：{:.2f}".format(sum/num))       #分母为0时程序有bug

print("*****************")
sum=0
salarys=[]
for x in range(4):
    a=input("请输入员工4名员工薪资（按Q或者q结束）")
    if a.upper()=="Q":
        print("录入完成，退出")
        break
    if float(a)<0:
        continue
    salarys.append(float(a))
    sum+=float(a)
else:
    print("您已经全部录入4名员工薪资")
print("录入薪资:",salarys)
print("平均薪资：{:.2f}".format(sum/4))



#嵌套循环测试

for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print()             #起到换行作用也可以写print("\n")



print("***************")
#这个是一个九九乘法表
#使用for循环嵌套实现
for x in range(1,10):
    for y in range(1,x+1):
        print("{}*{}={}".format(x,y,x*y),end=" ")
    print()

print("***********************************")
#使用while循环嵌套实现九九乘法表
x=1
while x<10:
    y=1
    while y<=x:
        print("{}*{}={}".format(x, y, x * y), end=" ")
        y=y+1
    print()
    x=x+1

print("**********")
#使用列表和字典存储表格数据
tb=[]
a1={"姓名":"高小一","年龄":18,"薪资":30000,"城市":"北京"}
a2={"姓名":"高小二","年龄":19,"薪资":20000,"城市":"上海"}
a3={"姓名":"高小三","年龄":20,"薪资":10000,"城市":"深圳"}
tb=[a1,a2,a3]
for x in tb:
    if x.get("薪资")>15000:
        print(x)







#打印一个坐标（x,y）象限
x=int(input("输入一个x坐标"))
y=int(input("输入一个y坐标"))

if x==0 and y==0:
    print("原点")
elif x==0:
    print("y轴")
elif y==0:
    print("y轴")
elif x>0 and y>0:
    print("第一象限")
elif x<0 and y>0:
    print("第二象限")
elif x<0 and y<0:
    print("第三象限")
elif x>0 and y<0:
    print("第四象限")

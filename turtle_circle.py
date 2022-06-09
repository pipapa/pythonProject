# 绘制不同颜色的多个同心圆_绘制弓箭靶
import turtle

t=turtle.Pen()

my_colors=("yellow","green","red","black")
t.width(2)
t.speed(0)
for x in range(10):
    t.pendown()
    t.color(my_colors[x%len(my_colors)])
    t.circle(10+x*10)
    t.penup()
    t.goto(0,-(10+x*10))

turtle.done()       #程序执行完，窗口不关闭




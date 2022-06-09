# 循环代码的优化测试
import time
shart= time.time()
for i in range(1000):
    result2 = []              #列表在for循环内只取最后一个值
    for m in range(10000):
        result2.append(i*1000+m*100)
end= time.time()
print("耗时：{0}".format((end-shart)))

shart2= time.time()

for i in range(1000):
    result2 = []
    c=i*1000
    for m in range(10000):
        result2.append(c+m*100)
end2= time.time()
print("耗时：{0:.2e}".format((end2-shart2)))





#4个九九乘法表

for x in range(1,10):
    for y in range(1,x+1):
        print("{}*{}={}".format(x,y,x*y),end="\t")
    print()



print("*************************")

s=[(x,y) for x in range(10) for y in range(10)]
print(s)

print([x for x in range(1,5)])


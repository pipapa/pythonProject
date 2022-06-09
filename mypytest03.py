#测试循环
num=0
while num<=10:
    print(num,end="\t")
    num+=1

print(end="\n")
#测试0～100之间的整数相加
num2=0
sum=0
while num2<=100:
    sum=sum+num2
    num2+=1
print("1-100之间整数相加值",sum)

#for 循环

for x in (20,30,40):
    print(x*3)

for x in "chen":
    print(x)
for x  in  [20,30,"chenjiansu"]:
    print(x)
a={"name":"cjs","age":32}
for x in a:
    print(x)
for x in a.keys():
    print(x)
for x in a.values():
    print(x)
for x in a.items():
    print(x)


#使用for循环求和0-100数字之间和
sum=0          #0~100累加和
sum1=0         #0～100奇数累加和
sum2=0         #0-100偶数累加和
for x in range(101):
    sum=sum+x
    if x%2==0:
        sum2=sum2+x
    else:
        sum1=sum1+x
print("0-100数字之间和为:",sum)
print("0-100数字之间奇数累加和:",sum1)
print("0-100数字之间偶数累加和:",sum2)

print("***************************")

#使用while循环求和0-100数字之间和
num=0
sum3=0
sum4=0
sum5=0
while num <=100:
    sum3 += num
    if num%2==0:
        sum5+=num
    if num%2==1:
        sum4+=num
    num += 1
print("0-100数字之间和为:",sum3)
print("0-100数字之间奇数和为:",sum4)
print("0-100数字之间偶数和为:",sum5)
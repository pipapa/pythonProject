money=1
seat=0
# money,seat = 1 表示有钱，有座位 0 表示没钱 没座位
if money == 1:
    print("可以做公交")
    if seat == 1:
        print('可以坐座位')
    else:
        print('就站着把')
else:
    print('没钱不能左公交')




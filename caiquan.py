'''
这是一个猜拳游戏
玩家vs机器随机
0代表剪刀，1代表拳头，2代表布
不允许出现平局
'''
import random
#导入随机模块

player = int(input('玩家出拳,0代表剪刀，1代表拳头，2代表布:'))
computer = random.randint(0,2)
# randint(a,b) 随机a~b之间的数
while True:
    if (player == 0 and computer == 2)  or (player == 1 and computer ==1) or (player ==2 and computer ==1):
        print('玩家获胜')
        break
    elif (player == 0 and computer == 0) or (player == 1 and computer == 1) or (player == 2 and computer == 2):
        print('电脑获胜')
        break
    else:
        print('平局')
        continue


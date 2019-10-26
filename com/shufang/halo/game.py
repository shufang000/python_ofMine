def start_game(money,numbers=3):
    if money == 0 :
        print('没钱还想押注？滚！')

    while True:
        if money == 0 :
            break
        pay = input('请输入你要压多少:')
        print('下注 ： {}元 买定离手'.format(pay))
        result = get_result(numbers,roll_dice(numbers))
        if result == 'BIG' :
            money += int(pay)
        else:
            money -= int(pay)
        print('顾客还剩{}元'.format(money))

import random
def roll_dice(numbers, points=None):
    print('<<<< ROLLING THE DICE!>>>>')
    if points is None:
        points = []
    if numbers < 3:
        print('骰子不足')
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers -= 1
    return points


def get_result(numbers, points):
    result = sum(points)
    if result > numbers * 6 / 2:
        return 'BIG'
    else:
        return 'SMALL'

start_game(1000)
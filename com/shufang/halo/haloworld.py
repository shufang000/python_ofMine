a = 1
print(a)
result = "elle" == 'Elle'
print(result)
print(abs(-10))  # 求绝对值

if 1 < 2:
    print("helloworld")

# 循环与判断
# 常用的条件判断符号 > < >= <= != ==,在python中可以连续比较如：1< 5<10 True
result = "Elle is My Firend" == "elle is my firend"
print(result)

# 不同类型之间不能用< > >= <= 但是可以用!=  ==
# print(42 < "helloworld")
print(42 != "helloworld")  # true
print(42 == "helloworld")

# true和false 分别代表1 0,可以进行隐式转换
print(True + False)  # 1
print(True > False)

# list 列表集合
list = ['hello', 'world', 21]
list.append('shufang')

print(list[0], list[-1])  ## hello shufang
print('shufang' in list)

the_ellie = 'Ellie'
name = 'Ellie'
print(the_ellie == name)  # True
print(the_ellie is name)  # True is就是用来校验的

# 在python中，除了0、None、[]、''、False,其他所有的对象都是True,可以用bool函数来判别
print(bool(''))  # False
print(bool([]))  # False
print(bool(0))  # False
print(bool(None))  # False
print(bool(False))  # False
print(bool(1))  # True

print(bool(1) + bool('hellworld'))  # 2

# boolean值之间的运算 关键字 or and not

print(1 < 2 or 3 > 5)  # True,类似于java中的｜｜
print(1 < 2 and 3 > 5)  # False，类似于java中的 &&
# 1<3and2<5 True
# 1<3and2>5 False
# 1<3or2>5 True
# 1>3or2>5 False

# if condtion:
#     do something

if not False:
    print("hello world!")
else:
    print("hello bitch!")

# def sout():
#     good = input("请输入数字：")
#     if int(good)%2 == 0 :
#         print("是偶数")
#     else:
#         print('是奇数')
#         sout()

#
# def sout():
#     good = input("请输入数字：")
#     result = good == '1234'
#     if result:
#         print("1234")
#     # elif:
#     #     print()
#     else:
#         print('not 1234')
#         sout()
#
#
# sout()
#
# here = input("please input from here:")
# if here == '1234':
#     print(here)
# elif here == '1235':
#     print(here)
# else:
#     print(int(here) + 1)  # 不同类型之间是不能进行运算的
#
# #  实现一个用密码登陆的功能
#
# print('------------------------------')
#
# passwdList = ['*#*#*', '12345']
#
#
# def account_login():
#     enter_pw = input("请输入密码：")
#     password_correct = enter_pw == passwdList[-1] # boolean类型
#     password_reset = enter_pw == passwdList[0]    # boolean类型
#     if password_correct:
#         print("Login correctlly!")
#     elif password_reset:
#         new_password = input("请输入一个新密码:")
#         # 将新密码添加到list中
#         passwdList.append(new_password)
#         print("添加新密码成功！")
#         account_login()
#     else:
#         print('输入的密码不正确，请重试')
#         account_login()
#
#
# # 切记，在python中,通过缩进代表层级关系
# account_login()
#
# # loop循环
# for i in [1,2,'helloworld!1234'
#               '1234',4,5]:
#     print(i)

tmp = 1
for i in range(1, 11):
    print(str(i) + ' + 1 =', i + 1)

songList = ['A Thousand Years', 'Pray', 'Holy Driver']
for song in songList:
    if song == 'A Thousand Years':
        print(song, '- Collie Meggen')
    elif song == 'Pray':
        print(song, '- Justin Bibber')
    elif song == 'Holy Driver':
        print(song, '- Dio')

for i in range(1, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i * j))

# while 循环
while i <= 100:
    print('still {}'.format(i))
    i += 1

    count = 0
while True:
    if count == 100:
        break
    print("happy programmer's day!")
    count += 1

passwordList = ['###', '123']  # 这里用到了闭包

print('-------------------')


# def account_login():
#     tries = 3
#
#     #  while 还可以结合 else一起使用
#     while tries > 0:
#         password = input('请输入密码：')
#         password_correct = password == passwordList[-1]
#         password_reset = password == passwordList[0]
#         if password_correct:
#             print("登陆成功！")
#             tries = 0
#         elif password_reset:
#             new_password = input('请重新输入新的密码：')
#             passwordList.append(new_password)
#             print("设置新密码成功！")
#             account_login()
#         else:
#             print("输入错误，请重试！")
#             tries -= 1
#             print()
#     else:
#         print("your account has been susppend!")
#
#
# account_login()


# for i in range(1,11):
#     file = open('/Users/shufang/Desktop/{}.txt'.format(i),'w')
#     file.write('helloworld')


def invest(amount, time, rate=0.05):
    for i in range(1, time + 1):
        amount = amount + amount * rate
        print(amount)


invest(10000, 10)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    else:
        print("{}不是偶数".format(i))

    # 求集合中元素的和，sum（），类似于scala中饿reduce
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(list1))
    print(min(list1))
    print(max(list1))

    import math
    import random

    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    c = random.randrange(1, 7)

    print(a, b, c)


# 模拟摇骰子
def roll_dice(numbers, points=None):
    print('starting rolling the dice！')
    tmp = numbers
    if points is None:
        points = []
    while numbers > 0:
        points.append(random.randrange(1, 7))
        numbers -= 1
    if (sum(points) > tmp * 6 / 2):
        print("BIG!")
    else:
        print('small~')


# roll_dice(3)
def start_game(numbers):
    dice_points = roll_dice(numbers)
    get_result(numbers,dice_points)


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
        print('BIG')
    else:
        print('SMALL')

start_game(3)
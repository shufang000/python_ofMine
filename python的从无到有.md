## python的小白学习方案

```python
# a=1
# print(a)
# s1 = "hello "
# s2 = "world"
# print(s1 + s2)
#
# # 这个w就是只有写的全线
# file = open("/Users/shufang/PycharmProjects/testPro/com/shufang/test1/com/shufang/test/hello.txt",'w')
# file.write("helloworld!")
#
# what_he_dos = "plays"
# his_instrument= 'guitar'
# is_name='ROBERT JOHNSON'
#
# art_show_is = is_name+' '+what_he_dos+' '+his_instrument
# print(art_show_is)
#
# num = 1;
# s= '1';
# print(num+int(s))
#
# result1 = len(is_name)+12
# print(result1)
#
#
#

string = 'thisworldwants to help me@®'
print(string[0])
print(string[-15:-12])
print(string[0:])
print(string[:-1])  # 一般是的左包右不包

# .fromat()来进行批处理,三种方式
print('{} a word she can get what she {} for'.format('With', 'came'))
print('{position} a word she can get what she {verb} for'.format(position='With', verb='came'))
print('{0} a word she can get what she {1} for'.format('With', 'came'))

# 从控制台打印
# input = input('please enter the word from here:')
# reallocation = ' this is the name of the world:{}'.format(input)
# print(reallocation)
a = 1 / 2 * (3 + 4) * 5
print(a)
b = 32 * 9 / 5 + 32
print(b)


def hello(arg1, arg2):
    return arg1 + arg2


print(hello('hello ', 'world'))


def this():
    return 'hello world bitch!'  # return前面必须缩进


print(this())


def tempetrue(C):
    print(str(C * 9 / 5 + 32) + 'F')
    return  # 返回值是none


tempetrue(35)


def changeWeight(w1):
    print(str(w1 / 1000) + 'kg')  # 一般一个函数只需要写好一个功能


changeWeight(1000)


# 函数练习，求直角三角形的第三条边

def getTheThirdLine(a: int, b: int):
    l1 = a * a
    l2 = b * b
    import math
    l3 = math.sqrt(l1 + l2)
    print('the third line is :' + str(l3))
    return


getTheThirdLine(3, 4)


# 函数的参数类型，位置参数、关键词参数

def hello(a, b, c):
    print(a, b, c)


hello(a=1, b=2, c=3)
hello(1, 2, 3)
hello(1, b=2, c=3)
hello(c=3, b=2, a=1)
# hello(c=3,a=2,1) #编译报错
hello(1, 2, c=3)


# 求梯形的面积

def tixing_area(base_up, base_down, height=3):
    print('   *', '  * *', '* * *', '  |  ', '\n')
    print(((base_up + base_down) * height / 2))
    return


tixing_area(1, 2, 3)

base_up = 1
base_down = 2
height = 3
tixing_area(height,base_down,base_up)

tixing_area(1,2) # 4.5 可以在传参数的时候就给height传入默认值
tixing_area(1,2,height=3)  # 4.5

## python常用的内置函数
# file = open("/Users/shufang/Desktop/python_ofMine/python的从无到有.md",'w') # 打开文件
# file.write() # 往文件里面写


def wirte_text():
    path = '/Users/shufang/Desktop/'
    name = 'hello1.txt'
    file = open(path+name,'w')  # w代表写入模式，如果存在这个文件就写入，否则就创建该文件
    file.write('hello world!bitch this is my name : '+name)
    file.close()  # 关闭文件的写入
    print('wirte done!')
    return

wirte_text() # hello world!bitch

# 敏感词过滤
def textfile_filter(word,censored_word = 'lame',change_word='Awesome'):
     a = word.replace(censored_word,change_word)
     print(a)

textfile_filter('Python is lame!')


## 方法的调用
def done_conflex(name,word):
    wirte_text()
    textfile_filter(word)
    return


# 常用的python符号
# + - * / %  // 取整除，返回商的整数部分 9//2 = 4，9.0 // 2.0 = 4.0  ** 幂：10 ** 2 = 100

print(9/2)
print(9//2)  # 4.5
print(9.0//2) # 4.0
print(9.9%2.0) # 取模
print(10**20) ## 求幂值

# TODO

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

# TODO
```


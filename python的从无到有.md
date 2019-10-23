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


```


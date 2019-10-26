# python数据结构

```python
# python中的数据结构,python中有4种数据结构：
# list（列表）、类似于scala中的List[Any]
# dict（字典）、类似于jsonMap {'key':'value'}
# tuple（元祖）、类似于scala中的元祖
# set（集合）、类似于java中的set

# list
# list中的所有元素都是可变的
# list中可以容纳python中的任何对象
# list中的元素是有序的、也就是说每一个元素都有一个位置

WEEK_LIST = ['monday', 'tuesday', 'wdensday', 'thursday', 'friday', 'saturday', 'sunday']
print(WEEK_LIST[0])

ALL_TYPE_LIST = [1, '2', 2.9, True, print(1), [1, 2], (1, 2), {'key': 'value'}]
print(ALL_TYPE_LIST[-1])

fruts = ['pineapple', 'pear']
# 插入

fruts.insert(8, 'big')  # 如果位置超出了list的下表限制，那么只能放在最后面一位了
fruts[1:1] = ['hello']  # 这个比较复杂，通过下表位置所有元素的代替，但是也能起到插入的效果
print(fruts)
fruts.remove('hello')  # 移除list中的指定元素
fruts.reverse()  # 反转链表
fruts[0] = 'shufang'
print(fruts)

# 链表的下表与字符串的下表是完全类似的
#   [1 ,2 ,4 ,7 , 8 ]
#    0  1  2  3   4
#    -5 -4 -3 -2  -1

list2 = [1, 2, 3, 4, 5]
print(list2[0:0])  # []
print(list2[0:-1])  # [1,2,3,4],包左不包右
list2[0] = 100000000
print(list2)
list2.extend([100, 1000])
print(list2)
del list2[0:1]  # 用del 关键字进行删除，可以批量删除，比remove()方便很多
print(list2)

# list.insert(1,'') # 往指定下表插入元素的方法，其他元素往右移动一位
# list.append()  # 添加一个元素到list中的方法
# list.extend('','','') # 添加多个元素到list中的方法
##### 在python中，True与False首字母必须大写


print('---------------------------------')

# dict 字典
# 在dict中数据必须是以键值对存在的
# 逻辑意义上讲，键是不能重复的，但是值是能重复的
# 字典中的key是无法修改的，而value是可变的，可以是任何对象

dict1 = {'bidu': 'baidu',
         'sina': 'xinlang',
         'yuku': 'youku'}
print(dict1)

print(dict1.get('bidu'))  # key的类型是有要求的
print(dict1['yuku'])  # 这样得到对应key的值，也是可以

dict1.update({'1': 'shufang', '2': 'lanyage'})  # 批量插入一个dict的所有元素到原油的集合中
dict1['time'] = 'helloworld'  # 这样也是可以插入的
dict1['time'] = 'h'  # 可以增加kv ，也可以修改已存在k的v

del dict1['time']  # 通过del 关键字进行删除k的kv对
# dict[0:4] # 这样是不行的，字典是不支持切片的
print(dict1)

# Set Set中的元素一般都是无序的，而且是不重复的,set是不能切片的，是不能索引的
set = {1, 2, 3, 4, 5, 5}
print(set)
set.add(100)
print(set)
set.discard(5)
print(set)

# 数据结构的技巧
# List排序
list4 = [8, 4, 29, 7, 2, 1]

print(sorted(list4, reverse=False))  # 倒序

list5 = [1, 2, 3, 4, 56, 8]

for a, b in zip(list4, list5):
    print(a, 'is', b)

t1 = []
for i in range(1, 11):
    t1.append(i)

# 推导方式，自动讲i append进t2  ,效率比上面的方式要高
t2 = [i for i in range(1, 11)]
print(t2)

import time

a1 = []
t0 = time.clock()
for i in range(1, 20000):
    a1.append(i)
print(time.clock() - t0, 'seconds process time')
# -----------------------------------------------
# 0.004357 seconds process time
#      差不多是节省了一般的时间，数据量越大，效果越明显
# 0.0021720000000000003 seconds process time

# list = [item*1 for item in _iter],列表推导，item还可以作运算的
# -----------------------------------------------
t1 = time.clock()  # 记录当前时间
a2 = [i for i in range(1, 20000)]
print(time.clock() - t1, 'seconds process time')

# 以下是常用的list的推导
l1 = [i * 2 + 1 for i in range(1, 11)]
print(l1)  # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

l2 = [i.lower() for i in 'ABCDEFGH']
print(l2)

l3 = [i for i in range(1, 11) if i % 2 == 0]  # 还可以项scala中添加循环守卫guard
print(l3)

# python数据结构中除了list可以作推导，dict字典也可以作推导，但是必须得是kv形式的返回值
# dict推导示例如下：
d1 = {i: i + 1 for i in range(4, 11)}
print(d1)
d2 = {i: j for i, j in zip(range(1, 11), range(5, 15))}
print(d2)
d3 = {i: j for i, j in zip(range(1, 5), 'ABCDE')}
print(d3)  # {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

# 循环获取list中的索引，用enumerate()找到list中不同item的index
l4 = [i for i in range(1, 11)]
for i, j in enumerate(l4):
    print(i, 'is', j)  # 此时 i 就是索引 ，j就是真实数据

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()

print(words)

# import string
# import math
# import random
# import time

path = '/Users/shufang/Desktop/Walden.txt'

#   这就有点类似与Cypher的语法

# wordcount常用到的函数有:open() read() split()  count(word) 用到的关键字：with as for in
# 用到的list的推导, import 常用的string math
with open(path,'r') as text: # 这里的with是关键字，有点类似于neo4j中的 load csv from as line
    words1 = text.read().split()
    print(words1)
    for word in words1:
        print('{}-{} times'.format(word,words1.count(word)))

# 由于上面的统计结果很怪，有些大小写不区分的都重复统计了，所以先进行预处理
# import string
# path = '/Users/Hou/Desktop/Walden.txt'
# with open(path,'r') as text:
# 下面这行代码很明显用到了list的推导
# words2 = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()] 5. words_index = set(words)
# counts_dict = {index:words.count(index) for index in words_index}
# for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True): 8. print('{} -- {} times'.format(word,counts_dict[word]))


```


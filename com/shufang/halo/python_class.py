class Cococola:  # 这是一个类，有相同特征的某类事物的抽象叫class

    # 这个make_of是可乐的属性
    make_of = ['sugar', 'water', 'caffeine', 'soda']

    #
    # def drink(self):  # 这个是Cococola的内部方法、也叫成员方法，这个self代表实例的本身
    #     print("Drink energy!~")

    def drink1(coke):  # 将上面的代码改这样也是不会出编译的是错误的，self可以用任何类似于coke这样的参数代替
        print("Drink energy!")

    def drink(self, how_much):

        if how_much == 'a sip':
            print('Cool!~')
        elif how_much == 'whole_botlle':
            print('holly shit!')


your_cola = Cococola()  # 创建一个可乐的对象
my_cola = Cococola()

print(your_cola == my_cola)  # False
print(your_cola)
print(my_cola)

print(your_cola.make_of)  # ['sugar', 'water', 'caffeine', 'soda']
print(Cococola.make_of)  # ['sugar', 'water', 'caffeine', 'soda']
# 上集回顾
list = [i for i in range(1, 11)]  # 创建一个列表，并且往中间添加元素
list.extend([11, 12])
list.extend(range(13, 20))  #

dict = {i: str(i) for i in range(1, 11)}  # 往一个字典中添加kv对，K是不能改的，不能重复，但是V都可以

print(list)
print(dict)

for element in Cococola.make_of:
    print(element)

cola_for_china = Cococola()
cola_for_china.logo_local = '可口可乐～'
print(str(cola_for_china.make_of) + '\t' + cola_for_china.logo_local)

# 通过一个实例来调用方法,而且创建的实例可以创建属于自己特有的属性；
instance = Cococola()
# instance.drink()
instance.drink1()
instance.drink('whole_botlle')  # holly shit


class PessiCola:
    make_of = ['Sugar', 'Water', 'Caffeine', 'Soda']

    # __init__方法是Python类中自带的方法，相当于随着类一起被加载的,类似于java中的构造函数
    def __init__(self, logo_name):  # 这个logo_name 相当于是构造函数的传值
        self.logo = logo_name
        # 全部是自动完成的，不需要手动用实例去调用，只需要创建对象，然后自动调用该方法
        for element in self.make_of:
            print('Pessi has {}'.format(element))

    def drink(self):
        print(self.logo)  # 百事可乐！～
        print('Thanks EveryOne! i love you all~')


# 到这里我发现一个问题，python中 【不存在】 方法的重载的概念： overload
pessi = PessiCola('百事可乐！～')
print(pessi.logo)  # '百事可乐！～'
pessi.drink()


# 这是定义的一个新的可口可乐的类
class New_cocacola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup'
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.logo = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))


# 下面设计到的是python中类的继承
class CaffeineFree(New_cocacola):  # class CaffeineFree(New_cocacola):代表继承了New_cocacola
    calories = 0  # 继承之后，重写属性
    ingredients = [  # 继承之后，重写属性override
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]


coke_a = CaffeineFree('咖啡因')
print(coke_a)
coke_a.drink()

coke_b = New_cocacola('HIgh calories~')
print(coke_b.calories)  # 140
New_cocacola.calories = 10000  # 当用类名直接修改属性时，修改的是全局属性
print(coke_b.calories)  # 10000
print(New_cocacola.calories)

coke_c = New_cocacola('C')
coke_d = New_cocacola('D')
coke_c.calories = 140
print(coke_c.calories)  # 不同对象属性的改动是相互没有影响的,也不会影响全局属性
print(coke_d.calories)
print(New_cocacola.calories)


## 测试属性的关系

class TestA:
    pro = 1
    def __init__(self):  # 改动的只是当前对象self的属性
        self.pro = 2
# 创建实例
a = TestA()

print(a.pro)  # 2
print(TestA.pro)  # 1


# 所有的类通过自带的__dict__方法用字典来存储 引用类、引用实例 的属性，如下：
#  {'__dict__': <attribute '__dict__' of 'TestA' objects>,
#  '__weakref__': <attribute '__weakref__' of 'TestA' objects>,
#  'pro': 1, '__init__': <function TestA.__init__ at 0x10273fd90>,
#  '__module__': '__main__', '__doc__': None}

#  {'pro': 2}
# 引用流程：a.pro -> 如果a.pro不为空->a.pro->引用成功 ;else  ->TestA.pro -> 引用成功;否则报错
print(TestA.__dict__)
print(a.__dict__)


a1 = 'String!'
a2 = 1
a3 = []
a4 = {}
# 通过type函数查看变量类型
print(type(a1),type(a2),type(a3),type(a4))

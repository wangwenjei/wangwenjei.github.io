"""
名称空间(namespace): 存放名字的地方,是对栈区划分,有了名称空间后就可以在栈区中存放相同的名字
    内置名称空间:
        存放的名字: 存放Python解释器内置的名字
        存活周期:   Python解释器启动则产生,关闭则销毁

    全局名称空间:
        存放的名字: 只要不是函数内定义,也不是内置的,剩下的都是全局名称空间的名字
        存活周期:   Python文件执行则产生,Python文件运行完毕后则销毁

    局部名称空间:
        存放的名字: 在函数调用时,运行函数体代码过程中产生的函数内的名字
        存活周期:   在函数调用时存活,函数调用完毕后则销毁

名字查找优先级:    以定义阶段为准,在当前所在位置向上一层一层查找


global与nonlocal
    global: 如果在局部想要修改全局的名字对应的值,需要用global
"""

x = 1


def func():
    global x  # 声明x这个名字是全局的名字,不要再新造名字
    x = 2
    print(x)


func()  # ==> 2
print(x)  # ==> 2

"""
闭包函数: 
    闭包函数 = 名称空间与作用域 + 函数嵌套 + 函数对象
    核心特点: 名字的查找关系是以函数定义阶段为准

    "闭": "闭"函数指的是该函数是内嵌函数
    "包": "包"函数指的是该函数包含对外层函数作用域名字的引用(不是对全局作用域)


为什么要用闭包函数:
    闭包函数提供了函数的调用方法,但是在行数的外部无法对函数的内部信息做修改,保证了函数方法的
"""


def f1():
    x = 111

    def f2():
        print('函数f2:', x)

    return f2


x = 222
f2 = f1()
f2()  # ==> 函数f2: 111


# 两种为闭包函数传值的方式:
#     方式一: 直接吧函数体需要的参数定义成形参
def f2(x):
    print(x)


f2(1)  # ==> 1


#     方式二:
def f1(x):
    def f2():
        print(x)

    return f2


f2 = f1(111)
f2()  # ==> 111

"""
函数递归调用:是函数嵌套调用的一种特殊形式
    具体是值:
        在调用一个函数的过程中有直接或间接地调用到本身
        递归的本质就是无限循环
    递归调用不应无限的调用下去,必须在满足某种条件下结束递归调用

    递归的两个阶段:
        回溯: 一层一层调用下去
        递推: 满足某种结束条件,结束递归调用,然后一层一层返回
"""
print('函数递归')

list1 = [1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]


def func(l):
    for i in l:  # i ==>  1 [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]
        if type(i) is list:
            func(i)  # func( [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]] )
        else:
            print(i)  # 1


func(list1)  # ==> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

"""
匿名函数:
    lambda用于定义匿名函数
    lambda x, y: x + y
"""

# 匿名函数
s = {'zbw': 100, 'jh': 200, 'lsy': 300, 'qcx': 50}


def func(k):
    return s[k]


res = max(s, key=func)
print(res)  # ==> lsy

res1 = max(s, key=lambda k: s[k])
print(res1)  # ==> lsy

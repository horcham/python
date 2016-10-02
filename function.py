#def 函数名(参数):  函数体
def sb(what):
    a = ['hi!,what are you  talking about? ']
    what = a + what
    return what 
sb(['hey!shit~'])           #['hi!,what are you  talking about?, 'hey!shit~']

#函数文档 
#函数中的''部分，是不会被输出的，要查看需通过"函数名".__ doc__来访问
def sb(what):
    '我想要模拟对话'            #此为函数文档，在第一行
    a = ['hi!,what are you  talking about? ']
    what = a + what
    return what 
sb(['hey!shit~'])               #['hi!,what are you  talking about?, 'hey!shit~']
sb.__doc__                      #输出'我想要模拟对话'
help(sb)						#输出'我想要模拟对话'

#函数默认值 
def sb(how = "plan B",word = "my way"): 

#收集参数，本质为打包为元组.当无法确定函数的参数需要多少个时，用*变量表示
def sb(*a):
    print("第一个参数为：",a[0])
    print("第二个参数为：",a[1])
    print("第三个参数为：",a[2])
    print('参数长度为:',len(a))
sb(1,2,3,4,5,6)
#第一个参数为： 1
#第二个参数为： 2
#第三个参数为： 3
#参数长度为: 6
def sc(*a,b):
    print("第一个参数为：",a[0])
    print("第二个参数为：",a[1])
    print("第三个参数为：",a[2])
    print('参数长度为:',len(a))
sb(1,2,3,4,5,6)                     #出错，b没有值，需要用关键字赋值
sb(1,2,3,4,5,6,b = 6)
#第一个参数为： 1
#第二个参数为： 2
#第三个参数为： 3
#参数长度为: 6


#可返回多个值，用列表即可
def back1():
    return[1,2,3]
back()                          #[1, 2, 3]
def back1():
    return 1,2,3 
back()                          #(1, 2, 3)  转化为元组

#####################
#内嵌函数及闭包 
#在函数中无法修改全局变量，若在函数中修改全局变量，用global
a = 5
def func1():
    a = 10
func1()
print(a)                        #5

a = 5
def func1():
    global a
    a = 10
func1()
print(a)                        #10

#内嵌函数，在函数中定义另一个函数,在函数外不能调用该函数
def func1():
    print('func1()正在被调用')
    def func2():
        print('func2()正在被调用')
    func2()
func1()
#func1()正在被调用
#func2()正在被调用

#闭包 
#不能在函数外部调用fun2(y)，其作用域只在于fun1(x)中
def fun1():
    x = [5]
    def fun2():
        x[0] *= x[0]
        return x[0]
    return fun2()
fun1()  				#25  

#使用nonlocal关键字，声明x是在fun1()中的。其作用与global相似，只是nonlocal用于函数中
def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()
fun1()                      #25   

#匿名函数 lambda ，函数名 = lambda 形参:所要返回的表达式
def ds(x):
    return 2 * x + 2
ds(5)                       #12
g = lambda x : 2 * x + 2
g(5)                        #12
def add(x,y):
    return x + y
add(5,7)                    #12
b = lambda x,y : x + y
b(5,7)                      #12

#filter() 过滤器
"""
filter(function or None，iterable) 
1） 若function为有，则将iterable中的数据代入到function中，过滤出True的对象并组合成列表 
2）若为none，则将iterable中Ture中的对象组合成列表
"""
filter(None,[1,0,False,True,9])                 #<filter object at 0x02FA1CF0>
list(filter(None,[1,0,False,True,9]))           #[1, True, 9]

#map() 映射 
#map(function, *iterable) 
#将iterable中的数据代入到function中，并把结果组成列表并返回 
list(map(lambda x:x%2,range(10)))
list(map(lambda x:x*2,range(10)))

#递归 函数内部调用函数 
#设置递归深度
import sys
sys.setrecursionlimit(n)        #n为层数
def recy(n):
    if n >= 1:
        return n * recy(n-1)
    else:
        return 1
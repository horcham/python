#整型 
int() 
#浮点型 
float() 
#布尔类型 
bool() 
#字符串
str() 

#查看变量的类型的函数 type(变量),isinstance(变量,类型)
a='520'
type(a)    #输出结果为 <type 'str'>
b=520
type(b)    #输出结果为 <type 'int'>
a=520
isinstance(a,int)   #输出结果为 true

#随机数
import random
a=random.randint(...)

#assert(逻辑值)
#当逻辑值为false时，马上崩溃报错。为真时程序才能工作，用于检验程序是否正确，正确则pass，错误时AssertionError
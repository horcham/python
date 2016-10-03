"""
异常值检测：try-except语句

try:
    检测范围
except Exception[as reason]:
    出现异常（Exception）后的处理代码
可与while和for搭配
"""

#1.else与while搭配 
#若while循环顺利结束之后，执行else，若是被break打断，则不执行else

a = int(input('输入一个数：'))
i = a 
while a >1:
    i -=1
    if a % i ==0 and i !=1: 
        print('最大公约数为：',i)
        break
else:
    print('为素数')
# 输入14时，返回7
# 输入11时，返回为素数


#2.else与for搭配，作用与while一样
a = int(input('输入一个数：'))
i = a 
for a in range(1,a):
    i -=1
    if a % i ==0 and i !=1: 
        print('最大公约数为：',i)
        break
else:
    print('为素数')



#3.可与try except语句搭配
a = input('输入一个数')
try:
    b = int(a)
except ValueError as reason:
    print('出错，需要数字,错误原因:')
else:
    b *= b
    print('a的平方为',b)
#输入字母A时，出错，需要数字,错误原因:invalid literal for int() with base 10: 'A'
#输入数字时，返回其平方值



#4.with .... as,可以防止缺少关闭文件操作
a = input('输入一个数')
try:
    b = int(a)
except ValueError as reason:
    print('出错，需要数字,错误原因:' + str(reason))
else:
    b *= b
    print('a的平方为',b,'已写入')
finally:
    c = open('E://2016.1//python//123.zhq','w')
    c.write(str(b))
    c.close()

#转换为

    a = input('输入一个数')
try:
    b = int(a)
except ValueError as reason:
    print('出错，需要数字,错误原因:' + str(reason))
else:
    b *= b
    print('a的平方为',b,'已写入')
finally:
    with(open('E://2016.1//python//123.zhq','w')) as c:
        c.write(str(b))
        c.close()
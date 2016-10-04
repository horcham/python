#字符串可进行切片，语法和元组一样
str = 'are you sure?'
str[:6]                 #输出'are yo'
str[6:]                 #输出'u sure?'
str[:]                  #输出'are you sure?'

#对字符串进行访问时，语法和元组一样
str = 'are you sure?'
str[0]                  #输出'a'

#对字符串进行修改时，采用元组的方法
str = 'are you sure?'
str + 'oh!'				#输出'are you sure?oh!'

#capitalize() 字符串首字母大写 
str = 'are you sure?'
str.capitalize()        #输出为'Are you sure?'

#casefold() 全部变为小写 
str = 'ARE YOU SURE?'
str.casefold()          #输出为'are you sure?'

#center(width) 用于居中，width为最大的填充长度 
str = 'ARE YOU SURE?'
str.center(20)          #输出为'   ARE YOU SURE?    '

#count(sub[,start[,end]]) 
#返回sub在字符串中出现的次数，start和end参数表示范围 
#语法:'数组名'.count(sub[,start[,end]])
str = 'ARE YOU SURE?'
str.count('RE')         #输出为2
str.count('RE',4,8)     #输出为0
str.count('RE',4)       #输出为1

#endswith(sub[,start[,end]]) 
#检验字符串是否以sub结束 
#语法:'数组名'.endswith(sub[,start[,end]])
str = 'ARE YOU SURE?'
str.endswith('RE',0,3)      #返回True
str.endswith('RE',0,4)      #返回False

#expandtabs([tabsize=8]) 
#将字符串中的tab符号(\t)换成为空格，如不指定参数，则默认空格数为tabsize=8
str = 'ARE\tYOU\tSURE?'
print(str)                  #返回ARE  YOU    SURE?
str.expandtabs()            #返回'ARE     YOU     SURE?'
str.expandtabs(10)          #返回'ARE       YOU       SURE?'

#find(sub[,start[,end]]) 
#判断sub是否在字符串中，是则返回索引值，没有则返回-1
str = 'ARE YOU SURE?'
str.find('T')               #返回-1
str.find('E')               #返回2
str.find('OU')              #返回5

index(sub[,start[,end]]) 
#与find类似，但sub不在字符串中会报错 
isalnum() 
#若字符串中至少有一个字符且所有字符都是字母或数字时，返回True，否则False 
isalpha() 
#字符串至少有一个字符且所有字符都是字母则返回True，否则False 
isdecimal() 
#字符串中只包含十进制数字时返回True，否则False 
isdigit() 
#字符串中只包含数字时返回True，否则False 
islower() 
#字符串中至少包含一个区分大小写的字符，且这些字符都是小写，则为True，否则False，中文为false 
isspace() 
#只有空格，则返回True，否则False 
istitle() 
#所有单词都以大写开头，其他均小写为True，否则False 
isupper() 
#所有字母都为大写，则返回True，否则False 
join(sub) 
#将字符串作为分隔符，插入到sub的所有字符之间
str = 'are'
str.join('0000')            #返回'0are0are0are0'

ljust(width) 
#返回一个左对齐的字符串，并用空格填充至长度为width 
lower() 
#转换字符串中所有大写字符为小写 


lstrip('str') 
#去掉字符串中左边的所有空格,有'str'则去除左边的'str'中的字符
rstrip('str') 
#去掉字符串中右边的所有空格,有'str'则去除右边的'str'中的字符 
strip('str')
#去掉字符串中右边的所有空格,有'str'则去除两边的'str'中的字符 


partition(sub) 
#以sub为中心，将字符串切割成左，中，右三个元组
str = 'ARE YOU SURE?'
str.partition('YO')         #结果为('ARE ', 'YO', 'U SURE?')

replace(old,new[,count]) 
#将字符串中old字符串替换成new字符串，若count给定时，则替换不超过count次 
rfind(sub[,strat[,end]]) 
#从右边开始查找find，判断sub是否在字符串中，是则返回索引值，没有则返回-1 
rindex(sub[,start[,end]]) 
#类似index方法，不过是向右开始 
rjust(width) 
#返回一个右对齐的字符串，并用空格填充至长度为width 
#类似的，有 
rpartition(sub) 
rstrip() 

split([sep=None,maxsplit=-1]) 
#自动切片，默认以空格进行切片
str = 'ARE YOU SURE?'
str.split()                 #结果为['ARE', 'YOU', 'SURE?']
str.split('R')              #结果为['A', 'E YOU SU', 'E?'],其中'R'被切割

startwith(prefix[,start[,end]]) 
#检查是否以prefix开头 

strip([chars]) 
#不带参数时，删除两边的空格，然而中间的空格不删除 ;带参数时，删除两边的指定参数
str1 = '    qqqqssssqqqq    '
str1.strip()                #结果为'qqqqssssqqqq'
str2 = 'qqqqssssqqqq'
str2.strip('q')             #结果为'ssss'

swapcase() 
#翻转字符串的大小写 
title() 
#将字符串中各首字母变成大写 

translate(table) 
#按规律转化 
#语法："字符串".translate(str.markrans('被转'，'想转为'))

str2 = 'qqqqssssqqqq'
str2.translate(str.maketrans('s','pp'))

format 
#"位置参数".format("字符串") 
#1）位置参数
"{0}.{1}.{2}.{3}".format('a','b','c','d')       #结果为'a.b.c.d'
"{0}{1}{2}{3}".format('a','b','c','d')      #结果为'abcd'
#2）关键字参数
"{a}{b}{c}{d}".format(a='a',b='b',c='c',d='d') 
#结果为'abcd'



#序列
#1.list([iterable]) 将可迭代对象转换成列表，其中iterable为迭代器
a = 'what is that!'
list(a)             #['w', 'h', 'a', 't', ' ', 'i', 's', ' ', 't', 'h', 'a', 't', '!']
b = (1,1,2,3,5,8,13,21)
list(b)             #[1, 1, 2, 3, 5, 8, 13, 21]
c = (1,1,2,3,5,8,13,21,'a',a)
list(c)             #[1, 1, 2, 3, 5, 8, 13, 21, 'a', 'what is that!']
#2.tuple([iterable]),同上

len(iterable) #返回对象长度
#max(iterable) 返回序列或参数集合中的最大值，字符时根据ASCII码，数字和字符串不能比较，要保证数据类型相同
d = ('a','b')
max(d)              #'b'
a = (97,'b')
max(a)              #出错
#min(对象)  返回序列或参数集合中的最小值，用法同max

#sum(iterable[,start=0])  从序列或参数集合所有相加后，再加上start，不能加字符串类型
f = (1,2)
f.extend([3,4,5,6])
f                   #[1, 2, 3, 4, 5, 6]
sum(f)              #21
sum(f,2)            #23

#sorted(iterable)  排序，默认从小往右排，用法与'列表'.list()用法一样
f = (1,2)
f.extend([3,4,5,6])
f                            #[1, 2, 3, 4, 5, 6]
f = f[:3]+[9,5,3]+f[3:]
f                            #[1, 2, 3, 9, 5, 3, 4, 5, 6]
sorted(f)                    #[1, 2, 3, 3, 4, 5, 5, 6, 9]
sorted(f,reverse=True)       #[9, 6, 5, 5, 4, 3, 3, 2, 1]

#reversed(iterable)   返回迭代器对象，其中的元素是逆转的，查看需放在list当中
f                           #[1, 2, 3, 9, 5, 3, 4, 5, 6]
reversed(f)                 #<list_reverseiterator object at 0x0323C070>
list(reversed(f))           #[6, 5, 4, 3, 5, 9, 3, 2, 1]

#enumerate(iterable)  返回迭代器对象，其中的元素是枚举的,其中是多个元组，查看需放在list当中
f                           #[1, 2, 3, 9, 5, 3, 4, 5, 6]
enumerate(f)                #<enumerate object at 0x02F82760>
list(enumerate(f))          #[(0, 1), (1, 2), (2, 3), (3, 9), (4, 5), (5, 3), (6, 4), (7, 5), (8, 6)]

#zip(iterable1，iterable2，...)   返回迭代器对象，其中的元素是对应在一起的组成元组，查看需放在list当中
f                           #[1, 2, 3, 9, 5, 3, 4, 5, 6]
a = [7,8,9,7,4,6]
b = [9,5,6,3,2,0,0]
zip(a,b,f)                  #<zip object at 0x02F82760>
list(zip(a,b,f))            #[(7, 9, 1), (8, 5, 2), (9, 6, 3), (7, 3, 9), (4, 2, 5), (6, 0, 3)]
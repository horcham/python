#大括号括入元素，则变成一个集合
a = {}
type(a)
#<class 'dict'>
b = {1,2,3}
type(b)
#<class 'set'>

#集合中元素具有唯一性
b = {1,2,2,2,3,3,3}
b   #{1, 2, 3}

#集合中元素具有无序性，不支持索引

#创建集合 
#同上，用大括号直接括起来 
#set(list/字符串/typle)
set1 = set([1,2,3,4,4])
set1
#{1, 2, 3, 4}

#访问集合中的值 
#可以用for将集合中的元素一个个读取出来
for eachset in c:
    print(eachset)   

#添加元素 
#集合.add(元素)
d = {1,2,3,4}
d.add(5)
d 		#{1, 2, 3, 4, 5}

#移除集合中的元素 
#集合.remove(元素)
d = {1,2,3,4}
d.remove(1)
d 		#{2, 3, 4}

#不可变集合，不能被添加，删除，修改 
#frozenset(list/字符串/typle)
i = frozenset([1,2,3,4])
i
i.add(5)    #报错
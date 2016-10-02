#当索引不好用时，采用字典
#将单词称为键，将其含义称为值
#字典的标志是大括号，其类型是映射

#索引方式如下
person = ['张三','李四','王五','小六']
slogan = ['学霸','花花公子','创作大神','节奏大师']
print('张三的标签是：',slogan[person.index('张三')])    #张三的标签是： 学霸

#字典方式如下 
dict2 = {1:'one',2:'two',3:'three',4:'four'}
dict2[2]                     #'two'

#创建字典的方式：
dict2 = {1:'one',2:'two',3:'three',4:'four'}
dict2[2]                     #'two'
# dict(mapping) 
dict3 = dict(((1,'one'),(2,'two'),(3,'three'),(4,'four')))
dict3[1]                    #'one'
dict5 = dict(张三='a',李四='b')
dict5                       #{'李四': 'b', '张三': 'a'}

# 字典名.fromkeys(S[,values]),重新创建新的字典
dict6 = {}
dict6 =dict6.fromkeys((1,2,3))
dict6                                        
#{1: None, 2: None, 3: None}
dict6.fromkeys((1,2,3),('what'))             
#{1: 'what', 2: 'what', 3: 'what'}
dict6.fromkeys((1,2,3),('what','is','that')) 
#{1: ('what', 'is', 'that'), 2: ('what', 'is', 'that'), 3: ('what', 'is', 'that')} 

#修改字典中的值
dict5 = dict(张三='a',李四='b')
dict5                       #{'李四': 'a', '张三': 'b}
dict5['张三']='c'
dict5                       #{'李四': 'a', '张三': 'c'}

#访问字典的key，value 

#字典名.keys(),访问key
dict5                       
#{'a': '1', 'b': '2', 'c': '3'}
dict5.keys()
#dict_keys(['a', 'b', 'c'])
for eachkey in dict5.keys():
    print(eachkey)    #a #b #c

#字典名.values() 访问value
dict5                       
#{'a': '1', 'b': '2', 'c': '3'}
dict5.values()
dict_values(['1', '2', '3'])
for eachvalues in dict5.values():
    print(eachvalues)  #1 #2 #3

#字典名.items() 打印key和value
dict5                       
#{'a': '1', 'b2': '2', 'c': '3'}
dict5.items()
dict_items([('a', '1'), ('b2', '2'), ('c', '3')])
for eachitems in dict5.items():
    print(eachitems)
#('a','1')
#('b','2')
#('c','3')

#字典名.get(key[,value0]) 访问key对应的value，当key不在其中时，则返回value0
dict5                       
#{'a': '1', 'b': '2', 'c': '3'}
dict5.get('c')
#'学霸'
dict5.get('d','没有值')
#'没有值'
dict5.get('c','没有值')
#'学霸'
'd' in dict5
#False
'c' in dict5
#True

#字典名.setdefault(key[,value0]) 
#访问key对应的value，当key不在其中时且没有value0时，添加该新的key且该key的value为None，当key不在其中时且有value0，则添加新的key且该key的value为value0

#清空字典。字典名.clear()，若令字典名={},只是改变字典名指向的位置
#字典拷贝。字典名.copy()，若对新的字典名进行同样的赋值,地址相同

#删除字典中的key和value 
#字典名.pop(key) 删除key以及对应的value，并返回
dict5                       
#{'a': '1', 'b': '2', 'c': '3'}
dict5.pop('c')
#'3'
dict5
#{'a': '1', 'b': '2'}

#字典名.popitem() 随机删除某个key以及对应的value，并返回
dict5 = dict( 'a'='1','b'='2','c'='3')
dict5                       
#{'c': '3', 'b': '2', 'a': '1'}
dict5.popitem()
#('c', '3')
dict5
#{'b': '2', 'a': '1'}


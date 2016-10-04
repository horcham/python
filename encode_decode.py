s = "你是谁"  #为GBK
s1 = u"你是谁" #为unicode
s2 = unicode("你是谁","utf-8")

su = "你是谁"
u = s.decode('utf-8')	#编码为unicode，给u
s = u.encode('gbk') 	#编码为gbk格式的字符串，赋给s


#python2.x
u = u'中文' #显示指定unicode类型对象u
str = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型


#python3.x
u = '中文' #指定字符串类型对象u
str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象u1
u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容


#decode用法
str.decode(encoding='UTF-8',errors='strict')
#encoding -- 这是所使用的编码。对于所有的编码方案的列表，请访问：标准编码库
#errors -- 这可能是给定一个不同的错误处理机制。默认的错误是“严格”，即编码错误提出UnicodeError。其他可能的值是ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 并通过codecs.register_error().注册的任何其他名称。
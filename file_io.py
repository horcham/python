"""
open()打开文件
open(file, mode='r',buffering=-1,encoding=None,errors=None, newline=None, closefd=True, opener=None) 
1）file为文件名，若不带路径，则在当前文件夹中寻找 
2）mode为文件打开模式 

打开方式，执行操作
r，以只读方式打开文件
w，已写入方式打开文件，会覆盖已存在的文件
x，如果问卷已经存在，使用此模式打开将引发异常
a，以写入模式打开，如果文件存在，则在末尾追加写入
b，以二进制模式打开
t，以文本模式打开
+，可读写模式
U，通用换行符支持

f.close() 关闭文件
f.read([size=-1])  从文件中读取size个字符，对于未给定size或给定负值时，读取剩余的字符，然后返回字符串
f.readline([size=-1])  按行读取
f.write(str)  将字符串str写入文件
f.writelines(seq)  向文件写入字符串序列
f.seek(offset,from)   在文件中移动文件指针，从from开始（0代表起始位置，1代表当前位置，2代表文件末尾），偏移offset个字节
f.tell()  			返回当前文件位置
t.truncate([size=file.tell()]) 		截取文件到size个字节
"""
open(f = open('../1.txt','r' ))
f.read(6)

"""
import os
getcwd() 		返回当前工作目录
chdir(path) 	改变工作目录
listdir(path='.')	列举指定目录的文件名('.'当前目录,'..'上一级目录)
mkdir(path) 	创建单层目录，如已存在则异常
makedirs() 		创建多层目录
remove(path) 	删除文件
rmdir(path) 	产出单层目录，若目录非空则异常
removedirs(path) 	递归删除目录，若目录非空则异常
rename(old,new) 	重命名
system(command) 	调用系统命令
walk(top) 		遍历所有子目录
os.curdir 		指代当前目录
os.pardir 		指代上一级目录
os.sep 			操作系统特定的路径分隔符
os.listsep 		当前平台使用的行终止符
os.name 		代指当前操作系统
"""

"""
basename(path) 	返回文件名
dirname(path) 	返回目录路径
join(path1,path2)	将path1和path2合成一个路径名
split(path) 	分割文件名和路径，返回(f_path,f_name)
splitext(path) 	分割文件名和拓展名，返回(f_name,f_extension)
getsize(file) 	返回文件尺寸，单位为字节
getatime(file) 	返回最近访问时间
getctime(file) 	返回创建时间
getmtime(file) 	返回最近修改时间
exists(path) 	是否存在
isabs(path) 	是否绝对路径
isdir(path) 	是否存在一个目录
isfile(path) 	是否存在一个文件
islink(path) 	是否符号链接
ismount(path) 	是否挂载点
samefile(path1,path2) 	path1和path2是否指向同一个文件

"""

#读取二进制数据 pickle
#存放文件
import pickle
list2 = [1,2,3,'what',(1,3,4),['right']]
list2_file = open('E://2016.1//python//list1_file.zhq','wb')
pickle.dump(list2,list2_file)
list2_file.close()
#读取文件
list3 = open('E://2016.1//python//list1_file.zhq','rb')
list4 = pickle.load(list3)
list4    #[1, 2, 3, 'what', (1, 3, 4), ['right']]

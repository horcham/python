#-*- coding:utf-8 -*-
import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import scoreatpercentile
data = np.loadtxt("test11.csv",delimiter=',',usecols=(1,),skiprows=1,unpack=True) #usecols为读取第2列，skiprows=1为跳过第一行
print(data)
print(1)  					#data的最大值
print(np.max(data)) 		#data的最大值
print(data.min())			#最小值
print(np.min(data))			#最小值
print(data.mean())			#平均值
print(np.mean(data))		#平均值
print(data.std())			#方差	
print(np.std(data))			#方差	
print(np.median(data))
print(sp.stats.scoreatpercentile(data,50))

#----------------------------
a = np.arange(9).reshape(3,3)  
#print(a)
b = np.hstack((a,a))
#print(b)
c = np.concatenate((a,a),axis=1)
#print(c)
d = np.vstack((a,a))
#print(d)
e = np.concatenate((a,a),axis=0)
#print(e)
f = np.dstack((a,a))
#print(f)
g1 = np.arange(3).reshape(3)
#print(g1)
#print(np.column_stack((g1,g1)))  #列式堆叠
print(np.row_stack((g1,g1)))	#行式堆叠
g2 = np.arange(6).reshape(2,3)
#print(g2)
#print(np.column_stack((g2,g2)))
print(np.row_stack((g2,g2)))

g3 = np.row_stack((g2,g2))
p1 = np.hsplit(g3,3)
p11 = np.split(g3, 3, axis = 1 )
p2 = np.vsplit(g3, 4)
print(p2)

#----------------------------
import numpy as np
b = np.arange(24).reshape(2,12)
print(b)
print(b.ndim)	#维度
print(b.size)	#元素个数
print(b.itemsize) #单个元素字节长度
print(b.nbytes)		#总共的字节数
print(b.reshape(4,6))	#调整为4*6矩阵
b = b.reshape(4,6)
print(b.T)		#转置
c = np.array([1.j+1,2.j+3]) #虚数矩阵
print(c.real) #返回实部
print(c.imag) #返回虚部

#迭代器遍历数组
f = b.flat  #迭代器
print (f)
for item in f:
	print (item)

print(b.flat[2]) #访问第3个元素
print(b.flat[[2,4]]) #访问第3,5个元素
b.flat[[2,4]] = [22,23] #将第3,5个元素分别改为22,23
print(b.flat[[2,4]])
b.flat = 0 #将所有元素改为0

#----------------------------
import numpy as np
b = np.array([1.+1.j,2.+3.j])
print(b)
print(type(b))
b1 = b.tolist() #将numpy转出list
print(b1)
print(type(b1))

c = b.astype(int) #将元素的复数类型转化为int
print(c)
c1 = c.astype(complex)  #将元素的int类型转化为复数
print(c1)

#----------------------------
import numpy as np
import scipy as sp
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import normaltest
import matplotlib.pyplot as plt
#二项分布
a = np.random.binomial(9, 0.1, size=1000)  #x~B(9,0.5)的10个样本
#print(a)

#正态分布
m = np.random.normal(0,1,size=4000)  #获得x~N(50，0.0001)的3个样本
dummy,bins,dummy = plt.hist(m,np.sqrt(10000),normed=False,lw=1)
plt.show()
#正态性检验
#shapiro
print("normal shapiro",shapiro(m))   #第一个值为检验统计量W，第二个值为p-value，当p-value<α=0.05(显著性水平时)，拒绝原假设H0：样本数据与正态分布没有显著区别  
print("normal anderson ",anderson(m))
print("normal normaltest",normaltest(m))  # pvalue>=0.5,则视为有正态性

#----------------------------
import numpy as np
import scipy as sp

#矩阵构建
A = np.array([[1,2],[3,4]])  #构建向量
A0 = np.matrix(A)	#将向量转为矩阵
B = np.arange(4).reshape(2,2)  #构建向量
B0 = np.matrix(B)	#将向量转为矩阵
C0 = np.mat("5,6;7,8")  #直接构建矩阵

#矩阵运算
A1 = np.linalg.inv(A)	#A求逆
I = A1*A0		#矩阵乘积
E = np.eye(3) 	#3*3的对角array向量

#解线性方程组 F*X=b
F = np.mat("1,-2,1;0,2,-8;-4,5,9")  #创建系数矩阵
#print(F)
b = np.array([0,8,-9])  #创建方程常数向量
X0 =np.linalg.solve(F, b)  #解出X
X = np.matrix(X0)			#将X转为矩阵
X = X.T					#将X转为列矩阵
#print(F*X)				#验证是否等于b
#print(np.dot(F, X0))			#	可代替代码22,23,24	

#求特征值和特征向量
Y = np.mat("3,-2;1,0")
print(np.linalg.eigvals(Y))	#特征值
[eigvalues,eigvectors] = np.linalg.eig(Y)	#返回特征值和特征向量
print("eigvalues")
print(eigvalues)	#特征值
print("eigvectors")
print(eigvectors)	#特征向量
#eigvalues[0] 和 [eigvectors[0,0],eigvectors[1,0]]一一配对

#--------------------------------
import numpy as np
b = np.array([1.+1.j,2.+3.j])
print(b)
print(type(b))
b1 = b.tolist() #将numpy转出list
print(b1)
print(type(b1))

c = b.astype(int) #将元素的复数类型转化为int
print(c)
c1 = c.astype(complex)  #将元素的int类型转化为复数
print(c1)

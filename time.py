#-*- coding:utf-8-*-
#时间元组
#gmtime(),localtime()和strptime()都以时间元组返回

import time 
a = time.gmtime()
print(a)
b = time.mktime(a)
print(b)
#分别代表：年、月、日、时、分、秒、星期、一年中第几天、夏令时
c = time.perf_counter()
print(c)
'''
time.altzone
#返回格林威治西部夏令时地区的偏移秒数
time.asctime([t])
#接受时间元组并返回一个可读取的形式为"Tue Dec 11 18:07:14 2015"
time.clock()
#用以浮点数计算的秒数返回当前的CPU时间
time.gmtime([secs])
#接受时间戳(1970后经过的浮点秒数)并返回格林威治时间下的时间元组t
time.localtime([secs])
#接受时间戳(1970后经过的浮点秒数)并返回当地时间下的时间元组t
time.mktime(t)
#接受时间元组并返回时间戳
time.perf_counter()
返回系统运行时间，包括系统睡眠时间
time.process_time()
返回当前进程执行CPU的时间总和，不包括睡眠时间
time.sleep(secs)
推迟条用线程的运行

'''

#定时器
import time as t
class Timer():
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0
    #是结果可以直接由对象直接调出来
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    #开始计时
    def start(self):
        self.start = t.localtime()
        self.prompt = '提示：先调用 stop()停止计时'
        print('计时开始..')
    #停止计时
    def stop(self):
        if not self.begin: #self.begin为0，不为真
            print('提示：先调用start()进行计时')
        else:
            self.stop = t.localtime()
            self._calc()
            print('计时结束..')
    #计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
    #为下一轮计时初始化变量
    self.begin = 0
    self.end = 0
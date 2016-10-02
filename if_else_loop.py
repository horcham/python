############if_else_loop##########

#if,else
#code1
x=5,y=0
if x>y；
    s=x
else
    s=y

#code1 can be simplified as code2
#code2
x=5,y=0
s=x if x>y else y

#some simple example
#code3
a=input("input one number")
if 0<a<=50:
    print("you are failed")
else:
    if 50<a<=80:
        print("middle")
    else:
        if 80<a<=100:
            print("good")
        else:
            print("error")

#code4 
a=input("input one number")
if 0<a<=50:
    print("you are failed")
if 50<a<=80:
    print("middle")
if 80<a<=100:
    print("good")
if a>100:
    print("error")

#code5	code5 is the same as code4
a=input("input one number")
if 0<a<=50:
    print("you are failed")
elif 50<a<=80:
    print("middle")
elif 80<a<=100:
    print("good")
else:
    print("error")


#while
#code6
a=0
i=0
while a!=3:
    a=input("请输入一个值")
    if a>3:
        print("too big")
    else:
        if a<3:
            print("too small")
        else:
            print("you win")
    i=i+1
    if i==3:
        print("you lose")
        break

#code7   code6 is the same as code7
i=0
a=0
while a!=3 and i!=3:
    a=input("请输入一个值")
    if a>3:
        print("too big")
    else:
        if a<3:
            print("too small")
        else:
            print("you win")
    i=i+1

#for 
#code8
range(1,5,2)  #输出一个数组[1,3]
range(5)      #输出一个数组[0,1,2,3,4]
for i in range(5):
    print(i)

#break
#code9
while TRUE:   
    if answer == a:
        break
    answer = input('请重新输入')

#continue
#code10
for i in range(10):
    if i%2 !=0:
        print(i)
        continue
    i += 2
    print(i)


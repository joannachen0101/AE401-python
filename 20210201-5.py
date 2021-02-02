import random
b=float(input('請輸入最大上限'))
s=float(input('請輸入最小下限'))
t=float(input('請輸入挑戰次數'))
num=random.randint(s,b)
a=float(input('What is the number?'))
while a!=num:
    if a>b or a<s:
        print('輸入錯誤')
        a=float(input('What is the number?'))
    elif num>a:
        t=t-1
        print('try again,It is too small,you have',t,'times')
        a=float(input('What is the number?'))
    elif num<a:
        t=t-1
        print('try again,It is too big,you have ',t,'times')
        a=float(input('What is the number?'))
if a==num:
        print('awesome')
if t==0:
    print('game over')

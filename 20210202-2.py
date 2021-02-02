import random
num=random.randint(1,11)
a=float(input('What is the number?'))
while a!=num:
        if num>a:
                print('try again,It is too small')
                a=float(input('What is the number?'))
        elif num<a:
                print('try again,It is too big')
                a=float(input('What is the number?'))
while a==num:
        print('awesome')
        break


        

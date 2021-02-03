m=[]
num=0
s=0
max=0
min=101
n=int(input('請問班上有幾個人?'))
while n!=num:
    num=num+1
    print('目前入到',num,'位同學')
    b=int(input('請輸入'))
    s=s+b
    m.append(b)
    print(m)
    if b>max:
        max=b
    if b<min:
        min=b
print('最高',max)
print('最低',min)
print('平均', s/n)  
        


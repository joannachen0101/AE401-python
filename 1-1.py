a={}
c=0
a['out']=0
y=list()
g=0
while True :
    print('1.設定')
    print('2進貨')
    print('3出貨')
    print('4營業額統計')
    print('5庫存統計')
    b=int(input('功能'))
    if b == 1 :
        num=int(input('有幾個蘋果'))
        a['s']=num
        m=int(input('一個多少錢'))
        print('有',num,'顆')
        print('一顆',m,'元')
    if b == 2 :
        add=int(input('進多少顆蘋果'))
        a['s']=a['s']+add
        print('進貨',add,'顆')
        print('有',a['s'],'顆')        
    if b == 3 :
        out=int(input('賣多少顆蘋果'))
        if a['out'] != 0 and c!= 1:
            a['out']=a['out']-out
            print('要付',out*m,'元','剩',a['out'],'顆')
            f=f+out
        elif c == 1 :
            a['out']=a['s']-a['out']-out
            print('要付',out*m,'元','剩',a['out'],'顆')
            f=f+out
        else:
            print('要付',out*m,'元','剩',a['s']-out,'顆')
            a['out']=out
            f=out
        c=c+1
        y.append(out)
    if b == 4 :
        for i in range(c):
            print(y[g],'顆',y[g]*m,'元')
            g=g+1
        print('共賣',f,'顆')
        print('營業額',f*m,'元')
    if b == 5 :
        print('剩',a['out'],'顆')
fo=open('myfile.txt','w')
fo.write('共賣',f,'顆')

fo=open('myfile.txt','r')

fo=open('myfile.txt','a')
fo.write('營業額',f*m,'元')
fo.write('剩',a['out'],'顆')

fo.close()

import os.path

if os.path.isfile('myfile.txt'):
        print('檔案存在')
else:
    print('檔案不存在')

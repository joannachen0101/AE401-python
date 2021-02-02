m=float(input('What is your math score?'))
e=float(input('What is your english score?'))
if m>=90 and e>=90:
    print('有獎品')
elif m<60 and e<60:
    print('要處罰')
elif m<60 or e<60:
    print('要加油')
else:
    print('')

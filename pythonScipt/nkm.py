def nkm(a,b):
   
    while a-b!=0:
        if(a<b):
            s=a
            a=b
            b=s
        c=a-b
        a=c
    print('最大公约数为',a)
m=int(input('请输入第一个数m：'))

n=int(input('请输入第二个数n：'))
if m!=0 and n!=0:
    nkm(m,n)
else:
    print('输入不合法！')

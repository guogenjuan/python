#辗转相除法
def maxYueshu(a,b):
    try:
        while a%b!=0:
            yushu=a%b
            shang=a//b
            a=b
            b=yushu
    except ZeroDivisionError:
        print('Error:Invalid argument')

    print('最大的公约数为'+str(b))


m=int(input('请输入第一个数字m：'))
n=int(input('请输入第一个数字n：'))

maxYueshu(m,n)

       

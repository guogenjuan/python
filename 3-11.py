def collatz(number):
    if number%2==0:
       # print('该数是偶数'+str(number))
        return number//2
    else:
        #print('该数是奇数'+str(number))
        return 3*number+1

a =0
while(collatz(a)!=1):
    print('请再次输入一个整数')
    try:
        a = int(input())
    except:
        print("必须输入一个整数!!!!")
print('恭喜'+str(collatz(a)))


num1=int(input("请输入一个数字"))
num2=int(input("请输入第二个数字"))

if num1<num2:
    smaller=num1
else:
    smaller=num2
for i in range(1,smaller+1):
    if num1%i==0 and num2%i==0:
        a=i
print("最大公约数是",a)

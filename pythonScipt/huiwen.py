str1=input("请输入几个字，判断是不是回文：")
a=str1[::1]
b=str1[::-1]
if a==b:
    print(str1,"是回文")
else:
    print("不是回文")

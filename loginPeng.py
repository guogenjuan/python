name="tarena"
pwd="123456"
i=3
while i>0:
    n = input("请输入用户名")
    p = input("请输入密码")
    if name==n and pwd==p:
        break
    i-=1
    print("输入错误，请重新输入")
if i==0:
    print("３次机会已经用完")
print("欢迎您回来")

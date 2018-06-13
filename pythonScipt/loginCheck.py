def loginCheck():
    count=0
    while  count<3:
        name=input('请输入用户名：')
        if name == 'tarena':
            pwd=input('请输入密码：')
            if pwd =='123456':
                print('欢迎您回来!')
                break
            else:
                count=count+1
                print('密码输入错误，请再次输入：')
        else:
            count=count+1
            print('用户名输入错误,请再次输入：')
    if count>=3:
        print('请找回用户名或密码！')
        
loginCheck()

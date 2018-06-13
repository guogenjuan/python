def mutiPlus():
    s=''
    for j in range(9):
        for i in range(9):
            if j>=i:
                s = (i+1)*(j+1)
                print(str(i+1)+'*'+str(j+1)+'='+str(s)+' ',end='')
        print()
                
mutiPlus()

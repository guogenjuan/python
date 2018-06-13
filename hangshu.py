def hangshu():
    count=0
    s=''
    for i in range(20):
        s = s+str(i+1)
        count=count+1
        if count%5 == 0:
            print(s)
            s=''
            continue

hangshu()

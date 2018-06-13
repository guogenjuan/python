def testPrint(a):
  
    for i in a:
        s=''
        for j in a:
            s =s+str(i+j-1)
        print(s)
        print()

a=[1,2,3,4,5]
count=5
    
testPrint(a)

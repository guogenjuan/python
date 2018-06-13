def listCode(spamPara):
    spamPara[-1]='and'+ ''+spamPara[-1]
    ss=''
    for i  in spamPara[0:-1]:
        ss=ss+i+','+''
    ss=ss+spamPara[-1]
    print(ss)
     
        
spam=['apples','bananas','tofu','cats']
listCode(spam)


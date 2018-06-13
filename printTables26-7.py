def widthMax(tableData):
    
    #算出行数
    x = len(tableData)
    #算出列数
    y = len(tableData[0])
    for i in range(x):
        colWidth=[]
        for j in tableData[i]:
            colWidth.append(len(j))#记录长度
            colWidth.sort()
        colWidth[i]= colWidth[-1]
        print(colWidth[i])      

Date=[['apple','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]

widthMax(Date)

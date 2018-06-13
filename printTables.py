def printTable(a,colWidthPara,xPara,yPara):
    for j in range(yPara):
        for i in range(xPara):
            print(a[i][j].rjust(colWidthPara[i]),end=' ')
        print()


tableData=[['apple','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
#算出行数
x = len(tableData)
#算出列数
y = len(tableData[0])
colWidth=[]
for i in range(x):
    spam=[]
    for j in tableData[i]:
        spam.append(len(j))#记录长度
        spam.sort()
    colWidth.append(spam[-1])
print(colWidth)
printTable(tableData,colWidth,x,y)

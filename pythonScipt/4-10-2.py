def netCode(gridPara):
    x=len(gridPara)
    y=len(gridPara[0])
    for i in range(y):
        for j in range(x):
            print(gridPara[j][i],end='')
        print()
          

grid=[['.','.','.','.','.','.'],
      ['.','0','0','.','.','.'],
      ['0','0','0','0','.','.'],
      ['0','0','0','0','0','.'],
      ['.','0','0','0','0','0'],
      ['0','0','0','0','0','.'],
      ['0','0','0','0','.','.'],
      ['.','0','0','.','.','.'],
      ['.','.','.','.','.','.']]

netCode(grid)

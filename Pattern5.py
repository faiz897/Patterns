
n = int(input())

rows = 1

while rows <= n:

    cols = 1
    spaces = rows - 1

    while spaces:
        print(" ", end="")
        spaces -= 1
    
    while cols <= n - rows + 1:
        print(rows + cols - 1, end="")
        cols+=1
    print()
    rows += 1
'''
1234
 234 
  34 
   4
'''
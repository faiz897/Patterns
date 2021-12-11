
n = int(input())

rows = 1

while rows <= n:

    cols = 1
    spaces = rows - 1
    
    while spaces:
        print(" ", end="")
        spaces -= 1
    while cols <= n - rows + 1:
        print(rows, end="")
        cols += 1
    print()
    rows += 1
'''
1111
 222
  33 
   4
'''



n = int(input())

rows = 1

while rows <= n:

    cols = 1
    spaces = n-rows

    while spaces:
        print(" ", end="")
        spaces -= 1

    while cols <= rows:
        print("*", end="")
        cols += 1 
    
    print()
    rows += 1
'''
   *
  **
 ***
****
'''

n = int(input())

rows = 1
count = 1
while rows <= n:

    cols = 1
    spaces = n - rows

    while spaces:
        print(" ", end="")
        spaces -= 1
    while cols <= rows:
        print(count, end="")
        count += 1
        cols += 1
    print()
    rows += 1
'''
   1
  23
 456
78910
'''    


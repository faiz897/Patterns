
n = int(input())

rows = 1

while rows <= n:
     
    cols = 1
    spaces = n - rows

    while spaces:
        print(" ",end="")
        spaces -= 1
    while cols <= rows:
        print(cols, end="")
        cols += 1
    
    start = rows - 1
    while start:
        print(start, end="")
        start -= 1

    print()
    rows += 1
'''
     1
    121
   12321
  1234321
 123454321
12345654321
'''

n = int(input())

rows = 1

while rows <= n:

    cols = 1
    while cols <= rows:
        print(chr(ord("A") + rows - 1), end="")
        cols += 1 
    print()
    rows += 1

'''
A
BB
CCC
DDDD
'''

n = int(input())

rows = 1
start = 'A'
while rows <= n:
    cols = 1
    while cols <= rows:
        print(start, end="")
        start = chr(ord(start) + 1)
        cols += 1
    print()
    rows += 1

'''
A
BC
DEF
GHIJ
'''
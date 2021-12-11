
n = int(input())

rows = 1
start = 'A'

while rows <= n:
    
    cols = 1
    while cols <= n:
        print(start, end="")
        start = chr(ord(start) + 1) 
        cols += 1
    print()
    rows += 1
'''
ABC
DEF
GHI
'''
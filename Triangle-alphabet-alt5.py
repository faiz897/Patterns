
n = int(input())

rows = 1

while rows <= n:

    cols = 1
    start = chr(ord("A") + n - rows)
    while cols <= rows:
        print(start, end='')
        start = chr(ord(start) + 1)
        cols += 1
    print()
    rows += 1
'''
D
CD
BCD
ABCD
'''
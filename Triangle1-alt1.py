
n = int(input())

rows = 1

while rows <= n:

    cols = 1
    while cols <= rows:
        print(cols, end="")
        cols += 1
    print()
    rows += 1

'''
1
12
123
1234
'''

n = int(input())

rows = 1
while rows <= n:

    cols = 1
    while cols <= rows:
        print(rows - cols + 1 , end=" ")
        cols += 1
    print()
    rows += 1

'''
1
21
321
4321
'''
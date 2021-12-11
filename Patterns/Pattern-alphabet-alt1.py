
n = int(input())

rows = 1

while rows <= n:

    cols = 1
    while cols <= n:
        print(chr(ord("A") + cols - 1), end="") 
        cols += 1
    print()
    rows += 1
'''
ABC
ABC
ABC
'''
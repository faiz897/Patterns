
n = int(input())

rows = 1

while rows <= n:

    cols = 1

    while cols <= rows:
        print(chr(ord('A')+ rows + cols - 2), end="")
        cols += 1
    print()
    rows += 1
'''
A
BC
CDE
DEFG
'''
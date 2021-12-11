
n = int(input())

rows = 1

while rows <= n:
    
    cols = 1
    while cols <= n - rows + 1:
        print(cols, end="")
        cols += 1

    stars1 = rows-1
    while stars1:
        print("*", end="")
        stars1 -= 1
    
    stars2 = rows-1
    while stars2:
        print("*", end="")
        stars2 -= 1
    
    start = cols - 1
    while start:
        print(start, end="")
        start -= 1

    print()
    rows += 1
    


'''
1234554321
1234**4321
123****321
12******21
1********1
'''
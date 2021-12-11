n = int(input("Enter the number of rows: "))

rows = 1

while rows <= n:

    cols = 1
    while cols <= n:
        print(cols, end="")
        cols = cols + 1    
    print()
    rows += 1

'''
123
123
123
'''
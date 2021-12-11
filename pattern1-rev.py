n = int(input("Enter the number of rows: "))

rows = 1

while rows <= n:

    cols = 1
    while cols <= n:
        print(n-cols+1, end="")
        cols += 1
    print()
    rows += 1

"""
321
321
321
"""

n = int(input("Enter the number of rows: "))

rows = 1
count = 1

while rows <= n:
    
    cols = 1
    while cols <= n:
        print(count, end=" ")
        count += 1
        cols += 1
    print()
    rows += 1

'''
123
456
789
'''
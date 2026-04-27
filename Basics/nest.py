for i in range(5):
    print(i)
    for j in range(3):
        print(j)


rows = 5  # number of rows

for i in range(rows):
    for j in range(rows):
        # Print * for first/last row OR first/last column
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # move to next line

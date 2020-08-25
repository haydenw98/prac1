for i in range(1, 21, 2):
    print(i, end=' ')
print()

# prints in increments of 10 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# 3rd number in range being -1 allows the code to count down from 20(first number given) in increments of -1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# an input is taken from the user and used to print the number of stars for number given
stars = int(input("stars: "))
for i in range(0, stars):
    print('*', end='')
print()

# 2 for loops are used to create the star pyramid effect by having one value grow by 1 each time the nestled for loop runs
stars = int(input("stars: "))
rows = 0
for i in range (0, stars):
    rows = rows + 1
    for i in range(0, rows):
        print('*', end='')
    print()

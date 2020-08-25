items = int(input("Number of items: "))
# while loop checks to make sure the user has input a number that is zero or higher
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
# if the number is valid the price is added together in a for loop the length of the number of item input
else:
    price = 0
    for i in range(0, items):
        price = price + float(input("Price of item: "))
print("Total price of " + str(items) + " is $" + str(price))

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print("bonus is $" + str(bonus))
    sales = float(input("Enter sales: $"))
else:
    print("Sales is negative.")

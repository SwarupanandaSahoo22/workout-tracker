#Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print()

print ("----- YOUR CART -----")

print()

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")
print()

print("===== THANKYOU FOR SHOPPING!❤️ =====")
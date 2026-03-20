# Concession Stand Program

menu = {"pizza": 3.00, 
        "nachos": 2.45,
        "popcorn": 6.00,
        "ham burger": 3.20,
        "cookies": 5.00,
        "soda": 2.30,
        "lemonade": 1.99}

cart = []
total = 0

print("========== MENU ==========")
for keys, value in menu.items():
    print(f"{keys:15}: ${value:.2f}")
    
print("=" * 26)

while True:
    food = input("""Select you item (press "q" to Quit): """).lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-" * 26)
for food in cart:
    total += menu.get(food)
    print(food)

print("-" * 26)
print(f"Your Total is: ${total}")
#Compund interest calculator

# Principle = 0
# Rate = 0
# Time = 0

# while True:
#     Principle = float(input("Enter the principle amount: "))
#     if Principle < 0:
#         print("Principle can't be less than zero")
#     else:
#         break

# while True:
#     Rate = float(input("Enter the interest rate(%): "))
#     if Rate < 0:
#         print("Rate can't be less than zero")
#     else:
#         break


# while True:
#     Time = int(input("Enter the time in year/s: "))
#     if Time < 0:
#         print("Time can't be less than zero")
#     else:
#         break


# total = Principle * pow((1 + Rate / 100), Time)
# print(f"Balance after {Time} year/s: ${total:.2f}")













# Revision

Principle = 0
Rate = 0
Time = 0
is_running = True

while is_running:
    Principle = float(input("Enter the principle amount: "))
    if Principle < 0:
        print("Principle can not be less than zero")
    else:
        break

while is_running:
    Rate = float(input("Enter the rate of interest(%): "))
    if Rate < 0:
        print("Rate can not be less than zero")
    else:
        break

while is_running:
    Time = int(input("Enter the time in year(s): "))
    if Time < 0:
        print("Time can not be less zero")
    else:
        break

total = Principle * pow((1 + Rate / 100), Time)
print(f"Balance after {Time} year/s will be ${total:.2f}")
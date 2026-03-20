#Weight convertor

Weight = float(input("Enter your weight: "))
unit = input("Kilograms or Punds? (K / L): ").capitalize()

if unit == "K":
    Weight = Weight * 2.20462
    unit = "Lbs"
    print(f"Your weight is: {round(Weight)} {unit}.")

elif unit == "L":
    Weight = Weight /  2.20462
    unit = "Kgs"
    print(f"Your weight is: {round(Weight)} {unit}.")

else:
    print(f"""Sorry, the "{unit}" is not valid.""")
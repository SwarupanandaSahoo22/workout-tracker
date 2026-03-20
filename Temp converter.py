Temperature = float(input("Enter the temperature: "))
Unit = input("Celcius or Fahrenheit? (C / F): ").upper()

if Unit == "C":
    Temperature = (Temperature * 1.8) + 32
    print(f"The converted temperature is: {round(Temperature, 2)} F")

elif Unit == "F":
    Temperature = (Temperature - 32) * 0.56
    print(f"The converted temperature is: {round(Temperature, 2)} C")

else:
   print(f""""{Unit}" is not a valid unit.""")
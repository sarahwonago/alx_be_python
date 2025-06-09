FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) 

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature.isDigit():
    if unit == "C":
        c_to_f = convert_to_fahrenheit(temperature)
        print(f"{temp} is {c_to_f}")

    elif unit == "F":
        f_to_c = convert_to_celsius(temperature)
        print(f"{temp} is {f_to_c}")
    else:
        print("Invalid unit. Please enter C or F.")
else:
    print("Invalid temperature. Please enter a numeric value.")



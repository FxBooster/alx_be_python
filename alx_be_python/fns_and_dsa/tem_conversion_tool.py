# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main user interaction
try:
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted}°F")
elif unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted}°C")
else:
    raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

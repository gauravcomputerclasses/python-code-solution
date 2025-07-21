# Take temperature in Celsius as input and convert it to Fahrenheit

# Get temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
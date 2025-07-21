# Input a float number and separate its integer and decimal parts

# Get a float number from the user
num = float(input("Enter a float number: "))

# Separate the integer and decimal parts
integer_part = int(num)
decimal_part = num - integer_part

# Display the results
print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part:.3f}")  # Rounded to 3 decimal places for clarity
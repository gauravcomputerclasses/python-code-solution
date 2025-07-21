# Ask the user for a number and print all operations: +10, –5, ×2, ÷3

# Get the number from the user
num = float(input("Enter a number: "))

# Perform the operations
add_10 = num + 10
subtract_5 = num - 5
multiply_2 = num * 2
divide_3 = num / 3

# Display the results
print(f"Original number: {num}")
print(f"Number + 10: {add_10}")
print(f"Number - 5: {subtract_5}")
print(f"Number × 2: {multiply_2}")
print(f"Number ÷ 3: {divide_3:.2f}")  # Rounded to 2 decimal places
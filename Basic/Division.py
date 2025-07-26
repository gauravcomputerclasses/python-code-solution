# Input two numbers and print the result of integer division and remainder

# Get the two numbers from user
num1 = int(input("Enter first number (dividend): "))
num2 = int(input("Enter second number (divisor): "))

# Calculate integer division and remainder
int_division = num1 // num2
remainder = num1 % num2

# Display the results
print(f"Integer division ({num1} // {num2}): {int_division}")
print(f"Remainder ({num1} % {num2}): {remainder}")
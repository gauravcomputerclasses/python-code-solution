# Question: Take a 3-digit number as input and print the sum of its digits.

# Taking input from user
num = int(input("Enter a 3-digit number: "))

# Extracting digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Calculating sum of digits
digit_sum = hundreds + tens + units

# Printing the result
print("Sum of digits:", digit_sum)

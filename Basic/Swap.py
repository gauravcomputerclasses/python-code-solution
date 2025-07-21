# Question: Swap two numbers using arithmetic operators (without using a third variable).

# Taking input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping using arithmetic operations
a = a + b
b = a - b
a = a - b

# Printing the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

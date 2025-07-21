# Question: Take Principal (P), Rate (R), and Time (T) as input and print the Simple Interest.
# Formula: Simple Interest = (P * R * T) / 100

# Taking input from user
P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time (T) in years: "))

# Calculating Simple Interest
SI = (P * R * T) / 100

# Printing the result
print("Simple Interest is:", SI)

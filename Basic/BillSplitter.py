# Take total bill amount and number of friends, then calculate how much each should pay

# Get the total bill amount from the user
total_bill = float(input("Enter the total bill amount: ₹"))

# Get the number of friends splitting the bill
num_friends = int(input("Enter the number of friends: "))

# Calculate how much each friend should pay
each_pays = total_bill / num_friends

# Display the result
print(f"Each friend should pay: ₹{each_pays:.2f}")  # Rounded to 2 decimal places for currency
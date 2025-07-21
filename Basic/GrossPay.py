# Take hourly wage and hours worked, then print gross pay

# Get input from user
hourly_wage = float(input("Enter your hourly wage: ₹"))
hours_worked = float(input("Enter hours worked: "))

# Calculate gross pay
gross_pay = hourly_wage * hours_worked

# Display the result
print(f"Your gross pay is: ₹{gross_pay:.2f}")
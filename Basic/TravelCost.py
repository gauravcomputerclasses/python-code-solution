# Question: Input distance (km) and fuel cost per km, then compute total travel cost.

# Taking input from user
distance = float(input("Enter distance in kilometers: "))
cost_per_km = float(input("Enter fuel cost per kilometer: "))

# Calculating total travel cost
total_cost = distance * cost_per_km

# Printing the total cost
print("Total travel cost is:", total_cost)

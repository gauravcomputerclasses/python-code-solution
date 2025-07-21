# Input the radius of a circle and print the area

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area using the formula: area = π * r^2
pi = 3.14159  # Approximate value of π
area = pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
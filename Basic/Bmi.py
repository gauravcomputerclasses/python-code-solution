# BMI Calculator: weight (kg) / height² (m²)

# Get inputs
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print result
print(f"BMI: {bmi:.1f}")  # Formatted to 1 decimal place
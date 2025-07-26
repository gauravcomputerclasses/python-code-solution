# Calculate paint needed for a wall area

# Get user inputs
wall_area = float(input("Enter wall area (sq ft): "))
coverage = float(input("Enter paint coverage (sq ft/liter): "))

# Calculate liters needed (rounded up to handle partial liters)
liters_needed = wall_area / coverage

# Print results
print(f"\nFor {wall_area} sq ft wall with {coverage} sq ft/liter coverage:")
print(f"Paint needed: {liters_needed:.2f} liters")

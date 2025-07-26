# Currency Converter: USD to Target Currency

# Get inputs
usd_amount = float(input("Enter USD amount: "))
exchange_rate = float(input("Enter exchange rate (1 USD = target currency): "))

# Calculate converted amount
converted_amount = usd_amount * exchange_rate

# Print result
print(f"Converted amount: {converted_amount:.2f}")
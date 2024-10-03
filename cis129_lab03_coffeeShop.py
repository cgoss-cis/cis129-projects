# cis129_lab03_coffeeShop.py
# Coffee Shop Simulator
# Asks the user for the number of coffee and muffins they are purchasing,
# calculates subtotal, adds 6% tax, and prints a receipt

# Prices of items
coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# Input: Number of coffees and muffins
num_coffee = int(input("Number of coffees bought?\n"))
num_muffin = int(input("Number of muffins bought?\n"))

# Calculations
subtotal_coffee = num_coffee * coffee_price
subtotal_muffin = num_muffin * muffin_price
subtotal = subtotal_coffee + subtotal_muffin
tax = subtotal * tax_rate
total = subtotal + tax

# Output: Display receipt
print("\n" + "*" * 39)
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffee} Coffee at ${coffee_price} each: ${subtotal_coffee:.2f}")
print(f"{num_muffin} Muffins at ${muffin_price} each: ${subtotal_muffin:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("*" * 39)

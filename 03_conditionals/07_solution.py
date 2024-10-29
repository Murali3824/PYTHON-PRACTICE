# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option
# for "Extra shot" of espresso.

order_size = input("enter your order size :")
extra_short = False

if extra_short:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"

print("Order: ", coffee)
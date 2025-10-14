squarem_price = 7.61
discount = 0.18
yard_size = float(input())
price = squarem_price * yard_size
discount_size = price * discount
discount_price = price - (price * discount)
print(f"The final price is {discount_price:.2f} lv.")
print(f"The discount is {discount_size:.2f} lv.")
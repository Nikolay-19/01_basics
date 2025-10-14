euro = 1.94

vegetable_price = float(input())
fruit_price = float(input())
vegetable_quantity = int(input())
fruit_quantity = int(input())

sub_total = vegetable_price * vegetable_quantity + fruit_price * fruit_quantity
total = sub_total / 1.94

print(f"{total:.2f}")

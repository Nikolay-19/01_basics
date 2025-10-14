pens_price = 5.8
markers_price = 7.2
detergent_price = 1.2

pens = int(input())
markers = int(input())
detergent = int(input())
discount_rate = int(input()) / 100

pre_discount = pens * pens_price + markers * markers_price + detergent * detergent_price
discount_size = pre_discount * discount_rate
total = pre_discount - discount_size

print(f"{total:.2f}")

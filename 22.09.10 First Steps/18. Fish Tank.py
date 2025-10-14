length = int(input())
height = int(input())
width = int(input())
decorations = float(input()) / 100

area = length * height * width
available_area = area - (area * decorations)
water_needed = available_area / 1000

print(f"{water_needed:.2f}")

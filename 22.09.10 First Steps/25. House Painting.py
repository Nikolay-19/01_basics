from typing import Tuple

green_consumption = 3.4
red_consumption = 4.3
door = 1.2 * 2
windows = 2 * 1.5 * 1.5

h_house = float(input())
length = float(input())
h_roof = float(input())

area_house = 2 * h_house * h_house - door + (2 * h_house * length - windows)
area_roof = float(2 * length * h_house) + (h_house * h_roof)
green_quantity = area_house / green_consumption
red_quantity = area_roof / red_consumption

print(f"{green_quantity:.2f}")
print(f"{red_quantity:.2f}")

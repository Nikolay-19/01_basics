import math
x = int(input())
y = float(input())
z = int(input())
workers_qt = int(input())

wine_x = x * 0.4
grapes = wine_x * y
wine_l = 2.5
wine_qt = grapes / wine_l
wine_sold = math.floor(abs(z - wine_qt))
wine_worker = wine_sold / workers_qt

if wine_qt < z:
    print(f"It will be a tough winter! More {wine_sold} liters wine needed.")
if wine_qt >= z:
    print(f"Good harvest this year! Total wine: {math.floor(wine_qt)} liters.")
    print(f"{math.ceil(wine_sold)} liters left -> {math.ceil(wine_worker)} liters per person.")
    
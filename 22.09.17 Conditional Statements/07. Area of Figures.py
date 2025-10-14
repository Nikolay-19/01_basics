from math import pi

figure = input()

if figure == "square":
    a = float(input())
    square_area = a * a
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    rectangle_area = a * b
    print(f"{rectangle_area:.3f}")
elif figure == "circle":
    r = float(input())
    circle_area = pi * r * r
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    a = float(input())
    ha = float(input())
    triangle_area = a * ha / 2
    print(f"{triangle_area:.3f}")
    
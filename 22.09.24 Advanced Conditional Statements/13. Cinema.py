movie = str(input())
rows = int(input())
columns = int(input())

premiere = 12
normal = 7.5
discount = 5
total = 0

if movie == "Premiere":
    total = rows * columns * premiere
elif movie == "Normal":
    total = rows * columns * normal
elif movie == "Discount":
    total = rows * columns * discount

print(f"{total:.2f} leva")

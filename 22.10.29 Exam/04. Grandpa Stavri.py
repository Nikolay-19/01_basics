length = int(input())
litres = 0
degrees = 0
degrees_average = 0
for a in range(1, length + 1):
    alcohol_qt = float(input())
    proof = float(input())
    litres += alcohol_qt
    degrees += proof * alcohol_qt
degrees_average = degrees / litres
print(f"Liter: {litres:.2f}\n"
      f"Degrees: {degrees_average:.2f}")
if  degrees_average< 38:
    print("Not good, you should baking!")
elif 38 <= degrees_average <= 42:
    print("Super!")
elif degrees_average > 42:
    print("Dilution with distilled water!")
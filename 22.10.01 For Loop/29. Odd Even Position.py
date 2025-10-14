import sys
a = int(input())
max_odd_number = -sys.maxsize
min_odd_number = sys.maxsize
max_even_number = -sys.maxsize
min_even_number = sys.maxsize
odd_sum = 0
even_sum = 0

for b in range(1, a + 1):
    c = float(input())
    if b % 2 != 0:
        odd_sum += c
        if c > max_odd_number:
            max_odd_number = c
        if c < min_odd_number:
            min_odd_number = c
    else:
        even_sum += c
        if c > max_even_number:
            max_even_number = c
        if c < min_even_number:
            min_even_number = c
            
if odd_sum == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={min_odd_number:.2f},")
    print(f"OddMax={max_odd_number:.2f},")
    
if even_sum == 0:
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={min_even_number:.2f},")
    print(f"EvenMax={max_even_number:.2f}")
    
a = int(input())
b = int(input())

for c in range(a, b + 1):
    hundred_thousands = c // 100000
    ten_thousands = (c // 10000) % 10
    thousands = (c // 1000) % 10
    hundreds = (c // 100) % 10
    tens = (c // 10) % 10
    units = c % 10
    sum_even = ten_thousands + hundreds + units
    sum_odd = hundred_thousands + thousands + tens
    
    if sum_even == sum_odd:
        print(c, end=" ")
        
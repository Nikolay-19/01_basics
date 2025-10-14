a = float(input())
coins = 0
b = a * 100

while b > 0:
    if b >= 200:
        b -= 200
    elif b >= 100:
        b -= 100
    elif b >= 50:
        b -= 50
    elif b >= 20:
        b -= 20
    elif b >= 10:
        b -= 10
    elif b >= 5:
        b -= 5
    elif b >= 2:
        b -= 2
    elif b >= 1:
        b -= 1
    else:
        break
    coins += 1
    
print(coins)

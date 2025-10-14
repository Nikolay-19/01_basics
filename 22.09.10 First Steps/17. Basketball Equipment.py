rate = int(input())

trainers = rate - rate * 0.4
clothes = trainers - trainers * 0.2
ball = clothes * 0.25
accessories = ball * 0.2

total = rate + trainers + clothes + ball + accessories

print(f"{total:.2f}")

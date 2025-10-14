V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

F = P1 * H + P2 * H
percent_P1 = (P1 * H / F) * 100
percent_P2 = (P2 * H / F) * 100
percent = F / V * 100
overflow = F - V

if percent > 100:
    print(f"For {H} hours the pool overflows with {overflow:.2f} liters.")
if percent <= 100:
    print(f"The pool is {percent:.2f}% full. Pipe 1: {percent_P1:.2f}%. Pipe 2: {percent_P2:.2f}%")
    
shirt_pr = float(input())
ball_goal = float(input())
shorts = shirt_pr * 0.75
socks = shorts * 0.2
trainers = 2 * (shirt_pr + shorts)
total = (shirt_pr + shorts + socks + trainers) * 0.85
diff = abs(ball_goal - total)
if total >= ball_goal:
    print(f"Yes, he will earn the world-cup replica ball!\n"
          f"His sum is {total:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.\n"
          f"He needs {diff:.2f} lv. more.")
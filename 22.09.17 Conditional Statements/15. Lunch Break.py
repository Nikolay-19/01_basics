from math import ceil
series = str(input())
ep_length = int(input())
break_length = int(input())

lunch = break_length / 8
rest = break_length / 4
time_watching = break_length - lunch - rest
time_left = ceil(abs(break_length - lunch - rest - ep_length))

if time_watching >= ep_length:
    print(f"You have enough time to watch {series} and left with {time_left} minutes free time.")
if time_watching < ep_length:
    print(f"You don't have enough time to watch {series}, you need {time_left} more minutes.")
    
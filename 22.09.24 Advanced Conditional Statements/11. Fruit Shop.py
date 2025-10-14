fruit = str(input())
day = str(input())
quantity = float(input())

banana_R = 2.5
banana_W = 2.7
apple_R = 1.2
apple_W = 1.25
orange_R = 0.85
orange_W = 0.9
grapefruit_R = 1.45
grapefruit_W = 1.6
kiwi_R = 2.7
kiwi_W = 3
pineapple_R = 5.5
pineapple_W = 5.6
grapes_R = 3.85
grapes_W = 4.2
total = 0

if fruit not in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]:
    print("error")
elif day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print("error")

elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        total = quantity * banana_R
    elif fruit == "apple":
        total = quantity * apple_R
    elif fruit == "orange":
        total = quantity * orange_R
    elif fruit == "grapefruit":
        total = quantity * grapefruit_R
    elif fruit == "kiwi":
        total = quantity * kiwi_R
    elif fruit == "pineapple":
        total = quantity * pineapple_R
    elif fruit == "grapes":
        total = quantity * grapes_R
    print(f"{total:.2f}")

elif day in ["Saturday", "Sunday"]:
    if fruit == "banana":
        total = quantity * banana_W
    elif fruit == "apple":
        total = quantity * apple_W
    elif fruit == "orange":
        total = quantity * orange_W
    elif fruit == "grapefruit":
        total = quantity * grapefruit_W
    elif fruit == "kiwi":
        total = quantity * kiwi_W
    elif fruit == "pineapple":
        total = quantity * pineapple_W
    elif fruit == "grapes":
        total = quantity * grapes_W
    print(f"{total:.2f}")
    
import math
tournament_qt = int(input())
score_start = int(input())
score_sub = 0
score = 0
won = 0

for a in range(1, tournament_qt + 1):
    stage = str(input())
    
    if stage == "W":
        score_sub += 2000
        won += 1
    if stage == "F":
        score_sub += 1200
    if stage == "SF":
        score_sub += 720
    score = score_start + score_sub
    
print(f"Final points: {score}")
print(f"Average points: {math.floor(score_sub / tournament_qt)}")
print(f"{won / tournament_qt * 100:.2f}%")

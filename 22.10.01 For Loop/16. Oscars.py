name = str(input())
temp_score = float(input())
jury_qt = int(input())
score = 0
score_jury = 0

for a in range(1, jury_qt + 1):
    jury_name = str(input())
    personal_score = float(input())
    score_jury += (len(jury_name) * personal_score) / 2
    score = temp_score + score_jury
    
    if score >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {score:.1f}!")
        break

else:
    print(f"Sorry, {name} you need {(1250.5 - score):.1f} more!")
    
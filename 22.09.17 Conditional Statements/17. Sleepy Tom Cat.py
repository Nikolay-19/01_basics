play_year = 30000
play_work = 63
play_weekend = 127
year = 365

weekends = int(input())

total = ((year - weekends) * 63) + weekends * 127
difference = abs(play_year - total)
diff_hours = difference // 60
diff_minutes = difference % 60

if total >= play_year:
    print("Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")
if total < play_year:
    print("Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")
    
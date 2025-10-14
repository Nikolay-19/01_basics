chrysanthemum = int(input())
rose = int(input())
tulips = int(input())
season = str(input())
holiday = str(input())

total = 0
assembly = 2

if holiday == "N":
    if season == "Spring" or season == "Summer":
        chrysanthemum_pr = 2
        rose_pr = 4.1
        tulips_pr = 2.5
    elif season == "Autumn" or season == "Winter":
        chrysanthemum_pr = 3.75
        rose_pr = 4.5
        tulips_pr = 4.15
    total = chrysanthemum * chrysanthemum_pr + rose * rose_pr + tulips * tulips_pr + assembly
    if tulips > 7 and season == "Spring":
        total = (total - assembly) * 0.95 + assembly
    if rose >= 10 and season == "Winter":
        total = (total - assembly) * 0.9 + assembly
    if chrysanthemum + rose + tulips > 20:
        total = (total - assembly) * 0.8 + assembly

elif holiday == "Y":
    if season == "Spring" or season == "Summer":
        chrysanthemum_pr = 2 * 1.15
        rose_pr = 4.1 * 1.15
        tulips_pr = 2.5 * 1.15
    elif season == "Autumn" or season == "Winter":
        chrysanthemum_pr = 3.75 * 1.15
        rose_pr = 4.5 * 1.15
        tulips_pr = 4.15 * 1.15
    total = chrysanthemum * chrysanthemum_pr + rose * rose_pr + tulips * tulips_pr + assembly
    if tulips > 7 and season == "Spring":
        total = (total - assembly) * 0.95 + assembly
    if rose >= 10 and season == "Winter":
        total = (total - assembly) * 0.9 + assembly
    if chrysanthemum + rose + tulips > 20:
        total = (total - assembly) * 0.8 + assembly

print(f"{total:.2f}")

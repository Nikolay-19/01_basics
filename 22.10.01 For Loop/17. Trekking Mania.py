groups_qt = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for a in range(1, groups_qt + 1):
    group_size = int(input())
    
    if group_size <= 5:
        mountain = "Musala"
        g1 += group_size
    if 6 <= group_size <= 12:
        mountain = "Montblanc"
        g2 += group_size
    if 13 <= group_size <= 25:
        mountain = "Kilimanjaro"
        g3 += group_size
    if 26 <= group_size <= 40:
        mountain = "K2"
        g4 += group_size
    if group_size >= 41:
        mountain = "Everest"
        g5 += group_size
        
total = g1 + g2 + g3 + g4 + g5
print(f"{g1/total*100:.2f}%")
print(f"{g2/total*100:.2f}%")
print(f"{g3/total*100:.2f}%")
print(f"{g4/total*100:.2f}%")
print(f"{g5/total*100:.2f}%")
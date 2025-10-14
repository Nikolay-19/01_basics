month = str(input())
length = int(input())

studio_pr = 0
apt_pr = 0
total_s = 0
total_a = 0

if month == "May" or month == "October":
    studio_pr = 50
    apt_pr = 65
    if length <= 14:
        total_a = apt_pr * length
    if length <= 7:
        total_s = studio_pr * length
    if 7 < length <= 13:
        total_s = studio_pr * length - (studio_pr * length * 0.05)
    if length > 14:
        total_s = studio_pr * length - (studio_pr * length * 0.3)
        total_a = apt_pr * length - (apt_pr * length * 0.1)
if month == "June" or month == "September":
    studio_pr = 75.2
    apt_pr = 68.7
    if length <= 14:
        total_s = studio_pr * length
        total_a = apt_pr * length
    if length > 14:
        total_s = studio_pr * length - (studio_pr * length * 0.2)
        total_a = apt_pr * length - (apt_pr * length * 0.1)
if month == "July" or month == "August":
    studio_pr = 76
    apt_pr = 77
    total_s = studio_pr * length
    if length <= 14:
        total_a = apt_pr * length
    if length > 14:
        total_a = apt_pr * length - (apt_pr * length * 0.1)

print(f"Apartment: {total_a:.2f} lv.")
print(f"Studio: {total_s:.2f} lv.")

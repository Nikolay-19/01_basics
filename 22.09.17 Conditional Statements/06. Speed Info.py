V = float(input())

if V <= 10:
    print("slow")
elif 10 <= V <= 50:
    print("average")
elif 50 <= V <= 150:
    print("fast")
elif 150 <= V <= 1000:
    print("ultra fast")
elif V >= 1000:
    print("extremely fast")
    
V = float(input())

if V <= 10:
    print("slow")
elif V <= 50:
    print("average")
elif V <= 150:
    print("fast")
elif V <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
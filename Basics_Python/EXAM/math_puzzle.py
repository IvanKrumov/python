key = int(input())

Cond1 = False
Cond2 = False

for a in range(1, 30 + 1):
    for b in range(1, 30 + 1):
        for c in range(1, 30 + 1):
            if a + b + c == key and a < b < c:
                sum_key = a + b + c
                print(f"{a} + {b} + {c} = {sum_key}")
                Cond1 = True
            elif a * b * c == key and a > b > c:
                sum_key2 = a * b * c
                print(f"{a} * {b} * {c} = {sum_key2}")
                Cond2 = True

if Cond1 == False and Cond2 == False:
    print("No!")

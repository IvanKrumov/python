key = int(input())

for a in range(1, 30 + 1):
    for b in range(1, 30 + 1):
        for c in range(1, 30 + 1):
            if a + b + c == key and a < b < c:
                sum_key = a + b + c
                print(f"{a} + {b} + {c} = {sum_key}")
            elif a * b * c == key and a > b > c:
                sum_key2 = a * b * c
                print(f"{a} * {b} * {c} = {sum_key2}")

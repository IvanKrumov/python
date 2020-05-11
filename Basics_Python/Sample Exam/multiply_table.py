n = int(input())

hundreds = n // 100
hun_mod = n % 100
tens = hun_mod // 10
ones = hun_mod % 10

new_number = int(f"{ones}{tens}{hundreds}")

for i in range(1, ones + 1):
    for j in range(1, tens +1):
        for l in range(1, hundreds + 1):
            print(f"{i} * {j} * {l} = {i*j*l};")
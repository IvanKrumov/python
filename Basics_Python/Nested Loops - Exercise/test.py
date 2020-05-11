N= int(input())

for i in range(1, 9):
    number = i + 3
    if N // number:
        print(number)
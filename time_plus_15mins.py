hrs = int(input())
min = int(input())

min_s = min + 15
hrs_s = hrs + 1


if min_s <= 59:
    if hrs <= 23:
        print(f'{hrs}:{min_s}')
    else:
        hrs = hrs % 24
        print(f'{hrs}:{min_s}')

elif min_s > 59:
    min_s = min_s % 60
    if hrs_s <= 23:
        if min_s >= 10:
         print(f'{hrs_s}:{min_s}')
        else:
         print(f'{hrs_s}:0{min_s}')
    elif hrs_s > 23:
        if min_s >= 10:
         hrs_s = hrs_s % 24
         print(f'{hrs_s}:{min_s}')
        else:
         hrs_s = hrs_s % 24
         print(f'{hrs_s}:0{min_s}')














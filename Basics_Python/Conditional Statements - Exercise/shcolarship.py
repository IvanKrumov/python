from math import floor

income = float(input())
aver_succ = float(input())
minimal_wadge = float(input())

soc_scholar = 0
exel_scholar = 0


if minimal_wadge > income:
    if aver_succ > 4.50:
        soc_scholar = floor(minimal_wadge * 0.35)

if aver_succ >= 5.50:
        exel_scholar = floor(aver_succ * 25)

if soc_scholar > exel_scholar:
        print(f'You get a Social scholarship {soc_scholar} BGN')
elif exel_scholar > soc_scholar:
        print(f'You get a scholarship for excellent results {exel_scholar} BGN')
else:
    print('You cannot get a scholarship!')






   # print('You cannot get a scholarship!')




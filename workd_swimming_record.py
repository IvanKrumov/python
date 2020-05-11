from math import floor
record = float(input())
distance = float(input())
time_1m = float(input())   #speed in m/s


adds = distance / 15
adds_r = floor(adds)
additional_time = adds_r * 12.5
t_1 = distance * time_1m
t = t_1 + additional_time
"""print(adds_r)
print(t_1)
print(t)"""

if t >= record:
    print(f'No, he failed! He was {(t - record):.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {t:.2f} seconds.')


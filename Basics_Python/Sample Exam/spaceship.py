from math import floor

width_ship = float(input())
lenght_ship = float(input())
hight_ship = float(input())
hight_astronaut = float(input())

volume_ship = width_ship * lenght_ship * hight_ship
volume_room = 2 * 2 * (hight_astronaut + 0.40)

count_astronaut = volume_ship / volume_room
count_astronaut = floor(count_astronaut)

if 3 <= count_astronaut <= 10:
    print(f"The spacecraft holds {count_astronaut} astronauts.")
elif count_astronaut <3:
    print(f"The spacecraft is too small.")
elif count_astronaut > 10:
    print(f"The spacecraft is too big.")

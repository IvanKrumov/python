from math import floor
name = input()
count_games = int(input())
points_total = 0

for i in range(1, count_games + 1):
    game_name = input()
    points = int(input())
    if game_name == "volleyball":
        points += 0.07 * points
        points_total += points
    elif game_name == "tennis":
        points += 0.05 * points
        points_total += points
    elif game_name == "badminton":
        points += 0.02 * points
        points_total += points

aver = points_total / count_games
aver_floor = floor(aver)
total_floor = floor(points_total)
#print(f"Aver points {aver_round}")
if aver_floor > 75:
    print(f"Congratulations, {name}! You won the cruise games with {total_floor} points.")
else:
    print(f"Sorry, {name}, you lost. Your points are only {total_floor}.")

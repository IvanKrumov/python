from math import floor

year = input()
p = int(input())
h = int(input())

games_Sofia = (48 - h) * 3 / 4

games_home_town = h

games_holidays = p * 2 / 3

games_total = games_Sofia + games_holidays + games_home_town

if year == "leap":
    games = games_total * 1.15
elif year == "normal":
    games = games_total

games1 = floor(games)

print(games1)


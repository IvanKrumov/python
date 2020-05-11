points_start = int(input())
points_per_turn = 0
points = 0
count = 0
while points_start >= 0:
    count += 1
    sector = input()
    points_per_turn = int(input())
    if sector == "number section":
        points += points_per_turn
    elif sector == "double ring":
        points += 2 * points_per_turn
    elif sector == "triple ring":
        points += 3 * points_per_turn


    elif sector == "bullseye":
        print(f"Congratulations! You won the game with a bullseye in {count} moves!")

    print(points_start)





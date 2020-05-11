floor = int(input())
room = int(input())
current_floor = 0
current_room = 0
index_room = ""
for current_floor in range(floor, 0, -1):
    for current_room in range(0, room):
        if current_floor == floor:
            index_room = "L"
            print(f"{index_room}{current_floor}{current_room}", end=" ")
        elif current_floor % 2 == 0:
            index_room = "O"
            print(f"{index_room}{current_floor}{current_room}", end=" ")
        elif current_floor % 2 != 0:
            index_room = "A"
            print(f"{index_room}{current_floor}{current_room}", end=" ")
    print()
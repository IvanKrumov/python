w = int(input())
l = int(input())
h = int(input())
V_room = w * l * h

is_done_moving = False
free_space = V_room
while free_space > 0:
    command = input()
    if command == "Done":
        is_done_moving = True
        break

    boxes_count = int(command)
    free_space -= boxes_count

if is_done_moving:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")

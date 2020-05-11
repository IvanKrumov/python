
action = ''
steps_total = 0
failed = False
success = True
while steps_total < 10000:
    steps = input()
    steps_total += int(steps)
   # success = True
    if action == "Going home":
        steps_home = input()
        steps_total += int(steps_home)
        if steps_total < 10000:
            failed = True
        else:
            success = True
if success:
    print("Goal reached!")
    print("Good job!")
else:
    print(f"{10000 - steps_total} more steps to reach goal.")
n = int(input())
command = " "
pastry_counter = 0

for i in range(1, n + 1):
    name = input()
    for p in range(1, 3 +1 ):
        if p == "cookies":
            counter_cookies = int(input())
            if p != "cookies":
                counter_cookies = 0
        elif p == "cakes":
            cakes_cookies = int(input())
            if p != "cakes":
                cakes_cookies = 0
        elif p == "waffles":
            waffles_cookies = int(input())
            if p != "waffles":
                waffles_cookies = 0



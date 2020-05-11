destination = input()
dates = input()
nights = int(input())

if "France" == destination:
    if "21-23" == dates:
        price = 30
    elif "24-27"== dates:
        price = 35
    elif "28-31" == dates:
        price = 40


elif "Italy" == destination:
    if "21-23" == dates:
        price = 28
    elif "24-27"== dates:
        price = 32
    elif "28-31" == dates:
        price = 39

if "Germany" == destination:
    if "21-23" == dates:
        price = 32
    elif "24-27"== dates:
        price = 37
    elif "28-31" == dates:
        price = 43

price = nights * price

print(f"Easter trip to {destination} : {price:.2f} leva.")
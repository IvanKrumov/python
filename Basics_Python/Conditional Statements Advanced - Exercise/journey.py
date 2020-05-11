budget = float(input())
season = str(input())    #summer or winter
destination = ""      #“Bulgaria", "Balkans” и ”Europe”
vacation = ""      #„Camp” и „Hotel”;

if budget <= 100:
    if season == "summer":
        budget = budget * 0.30
    elif season == "winter":
        budget = budget * 0.70
elif 1000 >= budget > 100:
    if season == "summer":
        budget = budget * 0.40
    elif season == "winter":
        budget = budget * 0.80
if budget > 1000:
    if season == "summer" or season == "winter":
        budget = budget * 0.90


if budget <= 100:
    destination = "Bulgaria"
elif 1000 >= budget > 100:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

if season == "summer" and destination != "Europe":
    vacation = "Camp"
elif destination == "Europe":
    vacation = "Hotel"
else:
    vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation} - {budget:.2f}")

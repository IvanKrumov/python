degrees = int(input())
time_of_day = str(input())
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if "Morning" == time_of_day:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif "Afternoon" == time_of_day:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif "Evening" == time_of_day:
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if "Morning" == time_of_day:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif "Afternoon" == time_of_day:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif "Evening" == time_of_day:
        outfit = "Shirt"
        shoes = "Moccasins"
elif 25 <= degrees:
    if "Morning" == time_of_day:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif "Afternoon" == time_of_day:
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif "Evening" == time_of_day:
        outfit = "Shirt"
        shoes = "Moccasins"


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
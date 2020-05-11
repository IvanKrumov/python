month = input()
nights = float(input())

room = ""
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

price_studio = nights * price_studio
price_apartment = nights * price_apartment


if 7 < nights < 14 and (month == "May" or month == "October"):
    price_studio = price_studio * 0.95
elif nights > 14 and (month == "May" or month == "October"):
    price_studio = price_studio * 0.70
elif nights > 14 and (month == "June" or month == "September"):
    price_studio = price_studio * 0.80

if nights > 14:
    price_apartment = price_apartment * 0.90


print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
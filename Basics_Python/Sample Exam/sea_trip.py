money_for_food_per_day = float(input())
money_for_sov_per_day = float(input())
money_for_hotel_per_day = float(input())

total_hotel = (money_for_hotel_per_day * 0.9) + (money_for_hotel_per_day * 0.85) + (money_for_hotel_per_day * 0.8)
total_fuel = 7 / 100 * 420 * 1.85
personal = 3 * (money_for_food_per_day + money_for_sov_per_day)
total_money = personal + total_hotel + total_fuel






print(f"Money needed: {total_money:.2f}")

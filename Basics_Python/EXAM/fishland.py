price_skumria_per_kg = float(input())
price_caca_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = price_skumria_per_kg * 1.60
safrid_price = price_caca_per_kg * 1.80
price_midi = 7.5

total = palamud_kg * palamud_price + safrid_kg * safrid_price + midi_kg * price_midi

print(f"{total:.2f}")
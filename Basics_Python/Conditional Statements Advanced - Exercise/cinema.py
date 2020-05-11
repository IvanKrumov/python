screening_type = input()
rows = int(input())
colomns = int(input())

capacity = rows * colomns
income = 0

if "Premiere" == screening_type:
    income = capacity * 12
elif "Normal" == screening_type:
    income = capacity * 7.50
elif "Discount" == screening_type:
    income = capacity * 5

print(f"{income:.2f} leva")
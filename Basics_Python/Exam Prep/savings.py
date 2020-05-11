income = float(input())
months = int(input())
personal = float(input())

saving_per_month = income - (income*0.3) - personal
percent_saving = saving_per_month / income * 100
print(f"She can save {percent_saving:.2f}%")
print(f"{months * saving_per_month:.2f}")
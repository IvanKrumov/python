product = str(input())
city = str(input())
amount = float(input())

if product == 'coffee':
    if city == 'Sofia':
        print(amount*0.50)
    elif city == 'Plovdiv':
        print(amount*0.40)
    elif city == 'Varna':
        print(amount * 0.45)
elif product == 'water':
    if city == 'Sofia':
        print(amount*0.80)
    elif city == 'Plovdiv':
        print(amount*0.70)
    else:
        print(amount * 0.70)
elif product == 'beer':
    if city == 'Sofia':
        print(amount * 1.2)
    elif city == 'Plovdiv':
        print(amount * 1.15)
    else:
        print(amount * 1.10)
elif product == 'sweets':
    if city == 'Sofia':
        print(amount * 1.45)
    elif city == 'Plovdiv':
        print(amount * 1.30)
    else:
        print(amount * 1.35)
else:
    if city == 'Sofia':
        print(amount * 1.60)
    elif city == 'Plovdiv':
        print(amount * 1.50)
    else:
        print(amount * 1.55)
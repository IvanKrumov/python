value = float(input())
unit_input = str(input())
unit_output = str(input())

if unit_input == "m":
    if unit_output == "mm":
        value = value * 1000
        print(f'{value:.3f}')
    #elif unit_input == unit_output:
    #   value = value
    else:
        value = value * 100
        print(f'{value:.3f}')
elif unit_input == "cm":
        if unit_output == "m":
            value = value / 100
            print(f'{value:.3f}')
        else:
            value = value * 10
            print(f'{value:.3f}')
elif unit_input == "mm":
    if unit_output == "m":
        value = value / 1000
        print(f'{value:.3f}')
    else:
        value = value / 10
        print(f'{value :.3f}')
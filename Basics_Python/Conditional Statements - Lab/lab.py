from math import pi
figure = str(input("Input figure: "))
if figure == "square":
    a = float(input("Side a: "))
    S = a*a
    print(f'{S:.3f}')
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    S = a * b
    print(f'{S:.3f}')
elif figure == "circle":
    r = float(input())
    S = pi * r * r
    print(f'{S:.3f}')
elif figure == "triangle":
    a = float(input())
    h = float(input())
    S = (a * h) / 2
    print(f'{S:.3f}')

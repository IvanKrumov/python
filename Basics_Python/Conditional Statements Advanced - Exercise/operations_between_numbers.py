N1 = int(input())
N2 = int(input())
operation = input()

res_plus = N1 + N2
res_min = N1 - N2
#res_dev = N1 / N2
res_mul = N1 * N2
#res_mod = N1 % N2

if operation == "+" and res_plus % 2 == 0:
    print(f"{N1} + {N2} = {res_plus} - even ")
elif operation == "+" and res_plus % 2 == 1:
    print(f"{N1} + {N2} = {res_plus} - odd ")

if operation == "-" and res_min % 2 == 0:
    print(f"{N1} - {N2} = {res_min} - even ")
elif operation == "-" and res_min % 2 == 1:
    print(f"{N1} - {N2} = {res_min} - odd ")

if operation == "*" and res_mul % 2 == 0:
    print(f"{N1} * {N2} = {res_mul} - even ")
elif operation == "*" and res_mul % 2 == 1:
    print(f"{N1} * {N2} = {res_mul} - odd ")

if (operation == "/" or operation == "%") and N2 == 0:
    print(f"Cannot divide {N1} by zero")
elif operation == "/":
    res_dev = N1 / N2
    print(f"{N1} / {N2} = {res_dev:.2f}")
elif operation == "%":
    res_dev = N1 % N2
    print(f"{N1} % {N2} = {res_dev}")


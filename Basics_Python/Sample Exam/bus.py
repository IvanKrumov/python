passangers_count = int(input())
stops_count = int(input())
counter = 0
passangers_in = 0
passangers_out = 0
passangers_out_total = 0
passangers_in_total = 0
kontrola_final = 0

while counter < stops_count:
    kontrola = 0
    counter += 1
    passangers_out = int(input())
    passengers_in = int(input())
    passangers_out_total += passangers_out
    passangers_in_total += passengers_in


    if counter % 2 == 1:
        kontrola = 2
    else:
        kontrola = -2
    kontrola_final += kontrola



passangers_count_total = passangers_count + passangers_in_total - passangers_out_total + kontrola_final

print(f"The final number of passengers is : {passangers_count_total}")




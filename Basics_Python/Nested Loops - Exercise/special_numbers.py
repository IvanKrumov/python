N = int(input())

for i in range(1111, 9999 + 1):

    thousands = i // 1000
    thousands_modul = i % 1000
    hundreds = thousands_modul // 100
    hundreds_modul = thousands_modul % 100
    tens = hundreds_modul // 10
    ones = hundreds_modul % 10

    while thousands != 0:
        if N % thousands == 0:
            th_ok = True
            while hundreds != 0:
                if N % hundreds == 0:
                    hun_ok = True
                    while tens != 0:
                        if N % tens == 0:
                            ten_ok = True
                            while ones != 0:
                                if N % ones ==0:
                                    ones_ok = True


            print(i)

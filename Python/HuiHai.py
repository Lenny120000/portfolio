"""
Jos numeron voi jakaa kolmella, tulostetaan Hui
Jos numeron voi jakaa viidellä, tulostetaan Hai
Molemmat = HuiHai
"""
numero = 0
while True:
    numero += 1
    if numero % 3 == 0 and numero % 5 == 0:
        print("HuiHai")
    elif numero % 3 == 0:
        print("Hui")
    elif numero % 5 == 0:
        print("Hai")
    else:
        print(numero)
    if numero == 100:
        break

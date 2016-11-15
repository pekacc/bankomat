class Banka:
    def __init__(ucet,heslo,suma,pokusy):
        ucet.heslo = heslo
        ucet.suma = suma
        ucet.pokusy = pokusy
ucty = list()
ucty.append(Banka(1234,0,3))

def pristup(i):
    while ucty[i].pokusy > 0 and ucty[i].pokusy < 4:
        vstup = int(input("Zadajte heslo: "))
        if int(vstup) == ucty[i].heslo:
            print("Pristup povoleny!")
            ucty[i].pokusy = 4;
        else:
            ucty[i].pokusy -= 1;
            print("Nespravne heslo!")
            print("Pocet zostavajucich pokusov: " + str(ucty[i].pokusy))
    if ucty[i].pokusy == 0:
        print("Zablokovany ucet!")
        return 0
    else:
        ucty[i].pokusy = 3
        return 1

def vUcte():
    i = int(input("Zadajte cislo uctu: "))
    akcia = pristup(i) 
    if akcia == 0: return
    while akcia > 0:
        akcia = int(input("1.Vlozit peniaze\n2.Vybrat peniaze\n3.Pozriet zostatok\n0.Ukoncit\n"))
        if akcia == 0: return
        if akcia == 1:
            suma = int(input("Zadajte sumu: "))
            ucty[i].suma += suma
            print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
        elif akcia == 2:
            suma = int(input("Zadajte sumu: "))
            if ucty[i].suma < suma:
                input("Nedostatocny kapital, operacia prerusena!\n")
            else:
                ucty[i].suma -= suma
                print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
        elif akcia == 3:
            print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
            input()

def vytvor():
    print("Vase cislo: " + str(len(ucty)))
    heslo = int(input("Zadajte Vas pin kod: "))
    ucty.append(Banka(heslo,0,3))
    print("Ucet uspesne vytvoreny!")

while(1):
    print("Vitajte v Banke")
    akcia = int(input("1. Vstupit do uctu \n2. Vytvorit ucet\n0. ukoncit\n"))
    if akcia == 1:
        vUcte()
    elif akcia == 2:
        vytvor()
    elif akcia == 0:
        break
print("Dovidenia!")

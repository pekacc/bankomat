class Banka:
    def __init__(ucet,heslo,suma,pokusy):
        ucet.heslo = heslo
        ucet.suma = suma
        ucet.pokusy = pokusy
ucty = list()
ucty.append(Banka(1234,0,3))
while(1):
    print("Vitajte v Banke")
    akcia = int(input("1. Vstupit do uctu \n2. Vytvorit ucet\n0. ukoncit\n"))
    if akcia == 1:
        i = int(input("Zadajte cislo uctu: "))
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
        else:
            if akcia == 0: break
            ucty[i].pokusy = 3
            while akcia > 0:
                print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
                akcia = int(input("1.Vlozit peniaze\n2.Vybrat peniaze\n0.exit\n"))
                if akcia == 0: break
                suma = int(input("Zadajte sumu: "))
                if akcia == 1:
                    ucty[i].suma += suma
                elif akcia == 2:
                    ucty[i].suma -= suma
    elif akcia == 2:
        print("Vase cislo: " + str(len(ucty)))
        heslo = int(input("Zadajte Vas pin kod: "))
        ucty.append(Banka(heslo,0,3))
        print("Ucet uspesne vytvoreny!")
    elif akcia == 0:
        break
print("Dovidenia!")
        

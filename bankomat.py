class Banka:
    jazyk = 1
    def __init__(ucet,heslo,suma,pokusy,cislo):
        ucet.heslo = heslo
        ucet.suma = suma
        ucet.pokusy = pokusy
        ucet.cislo = cislo

ucty = list()

file = open("ucty.txt", "r")
a = file.readline()
while a != "":
    b = file.readline()
    c = file.readline()
    d = file.readline()
    ucty.append(Banka(int(a),int(b),int(c),int(d)))
    a = file.readline()

def vypisUcty():
    for i in range (0,len(ucty)):
        print (str(ucty[i].heslo))
    print()
def cisloUctu(cislo):
    for i in range (0,len(ucty)):
        if ucty[i].cislo == cislo: return i
    return -1

def zmenJazyk():
    i = int(input("1.Slovencina\n2.English\n"))
    if (i == 1) or (i == 2):
        Banka.jazyk = i
        if Banka.jazyk == 1: input("Jazyk uspesne zmeneny!\n")
        elif Banka.jazyk == 2: input("Language succesfully changed!\n")
    else:
        print("Invalid choice")

def pristup(i):
    while ucty[i].pokusy > 0 and ucty[i].pokusy < 4:
        if Banka.jazyk == 1: vstup = int(input("Zadajte heslo: "))
        if Banka.jazyk == 2: vstup = int(input("Enter you password: "))
        if int(vstup) == ucty[i].heslo:
            if Banka.jazyk == 1: print("Pristup povoleny!")
            if Banka.jazyk == 2: print("Access granted!")
            ucty[i].pokusy = 4;
        else:
            ucty[i].pokusy -= 1;
            if Banka.jazyk == 1:
                print("Nespravne heslo!")
                print("Pocet zostavajucich pokusov: " + str(ucty[i].pokusy))
            if Banka.jazyk == 2:
                print("Invalid password!")
                print("Remaining attempts: " + str(ucty[i].pokusy))
    if ucty[i].pokusy == 0:
        if Banka.jazyk == 1: input("Zablokovany ucet!")
        if Banka.jazyk == 2: input("Acount blocked!")
        return 0
    else:
        ucty[i].pokusy = 3
        return 1

def vUcte():
    if Banka.jazyk == 1: i = cisloUctu(int(input("Zadajte cislo uctu: ")))
    if Banka.jazyk == 2: i = cisloUctu(int(input("Enter account numer: ")))
    if i == -1:
        if Banka.jazyk == 1: input("Neexistujuci ucet!")
        if Banka.jazyk == 2: input("Non existing account!")
        akcia = 0
    else: akcia = pristup(i) 
    if akcia == 0: return
    while akcia > 0:
        if Banka.jazyk == 1: akcia = int(input("1.Vlozit peniaze\n2.Vybrat peniaze\n3.Pozriet zostatok\n0.Odhlasit sa\n"))
        if Banka.jazyk == 2: akcia = int(input("1.Deposit money\n2.Withdraw money\n3.Check balance\n0.Log out\n"))
        if akcia == 0: return
        if akcia == 1:
            if Banka.jazyk == 1: suma = int(input("Zadajte sumu: "))
            if Banka.jazyk == 2: suma = int(input("Enter the amount: "))
            ucty[i].suma += suma
            if Banka.jazyk == 1: print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
            if Banka.jazyk == 2: print("Account balance:" + str(ucty[i].suma) + "€\n")
        elif akcia == 2:
            if Banka.jazyk == 1: suma = int(input("Zadajte sumu: "))
            if Banka.jazyk == 2: suma = int(input("Enter the amount: "))
            if ucty[i].suma < suma:
                if Banka.jazyk == 1: input("Nedostatocny kapital, operacia prerusena!\n")
                if Banka.jazyk == 2: input("Insufficient balance, transaction cancelled\n")
            else:
                ucty[i].suma -= suma
                if Banka.jazyk == 1: print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
                if Banka.jazyk == 2: print("Account balance:" + str(ucty[i].suma) + "€\n")
        elif akcia == 3:
            if Banka.jazyk == 1: print("Zostatok na ucte: " + str(ucty[i].suma) + "€\n")
            if Banka.jazyk == 2: print("Account balance:" + str(ucty[i].suma) + "€\n")
            input()

def vytvor():
    if Banka.jazyk == 1: 
        cislo = int(input("Zadajte cislo Vasho noveho uctu: "))
        heslo = int(input("Zadajte Vas pin kod: "))
    if Banka.jazyk == 2: 
        cislo = int(input("Set you new account number: "))
        heslo = int(input("Enter your pin: "))
    ucty.append(Banka(heslo,0,3,cislo))
    if Banka.jazyk == 1: input("Ucet uspesne vytvoreny!")
    if Banka.jazyk == 2: input("Account succesfully created!")

while(1):
    if Banka.jazyk == 1: 
        print("Vitajte v Banke")
        akcia = int(input("1. Vstupit do uctu \n2. Vytvorit ucet\n3. Zmenit jazyk\n0. Ukoncit\n"))
    elif Banka.jazyk == 2: 
        print("Welcome to the Bank")
        akcia = int(input("1. Entry the account \n2. Create new account\n3. Change language\n0. Exit\n"))
    if akcia == 1:
        vUcte()
    elif akcia == 2:
        vytvor()
    elif akcia == 3:
        zmenJazyk()
    elif akcia == 9:
        vypisUcty()
    elif akcia == 0:
        break

file = open("ucty.txt", "w")
for i in range (0,len(ucty)): 
    file.write(str(ucty[i].heslo) + "\n" + str(ucty[i].suma) + "\n" + str(ucty[i].pokusy) + "\n" +  str(ucty[i].cislo) + "\n")
file.close()
if Banka.jazyk == 1: print("Dovidenia!")
elif Banka.jazyk == 2: print("See you soon!")

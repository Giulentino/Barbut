#2020  Giulentino  - Barbut pentru toti romanii
import random
optiune=int(input("⚀ La mai mica - apasa 1" "\n" "⚅ La mai mare - apasa 2" "\n" "  ""Iesi - apasa 0" "\nAlege:"))

sarezaru1=random.randint(1, 6)
sarezaru2=random.randint(1, 6)
sarezaru3=sarezaru=random.randint(1, 6)
sarezaru4=sarezaru=random.randint(1, 6)

###fct la mai mica
def zaru1jucator():
    global logozar1
    if sarezaru1==1:
        logozar1="⚀"
    elif sarezaru1==2:
        logozar1="⚁"
    elif sarezaru1==3:
        logozar1="⚂"
    elif sarezaru1==4:
        logozar1="⚃"
    elif sarezaru1==5:
        logozar1="⚄"
    elif sarezaru1==6:
        logozar1="⚅"


def zaru2jucator():
    global logozar2
    if sarezaru2==1:
        logozar2="⚀"
    elif sarezaru2==2:
        logozar2="⚁"
    elif sarezaru2==3:
        logozar2="⚂"
    elif sarezaru2==4:
        logozar2="⚃"
    elif sarezaru2==5:
        logozar2="⚄"
    elif sarezaru2==6:
        logozar2="⚅"


def zaru1calculator():
    global logozar3
    if sarezaru3==1:
            logozar3="⚀"
    elif sarezaru3==2:
            logozar3="⚁"
    elif sarezaru3==3:
            logozar3="⚂"
    elif sarezaru3==4:
            logozar3="⚃"
    elif sarezaru3==5:
            logozar3="⚄"
    elif sarezaru3==6:
            logozar3="⚅"

def zaru2calculator():
    global logozar4
    if sarezaru4==1:
        logozar4="⚀"
    elif sarezaru4==2:
        logozar4="⚁"
    elif sarezaru4==3:
        logozar4="⚂"
    elif sarezaru4==4:
        logozar4="⚃"
    elif sarezaru4==5:
        logozar4="⚄"
    elif sarezaru4==6:
        logozar4="⚅"

### fct la mai mare
def zaru3jucator():
    global logozar5
    if sarezaru1==1:
        logozar5="⚀"
    elif sarezaru1==2:
        logozar5="⚁"
    elif sarezaru1==3:
        logozar5="⚂"
    elif sarezaru1==4:
        logozar5="⚃"
    elif sarezaru1==5:
        logozar5="⚄"
    elif sarezaru1==6:
        logozar5="⚅"

def zaru4jucator():
    global logozar6
    if sarezaru2==1:
        logozar6="⚀"
    elif sarezaru2==2:
        logozar6="⚁"
    elif sarezaru2==3:
        logozar6="⚂"
    elif sarezaru2==4:
        logozar6="⚃"
    elif sarezaru2==5:
        logozar6="⚄"
    elif sarezaru2==6:
        logozar6="⚅"

def zaru5calculator():
    global logozar7
    if sarezaru3==1:
        logozar7="⚀"
    elif sarezaru3==2:
        logozar7="⚁"
    elif sarezaru3==3:
        logozar7="⚂"
    elif sarezaru3==4:
        logozar7="⚃"
    elif sarezaru3==5:
        logozar7="⚄"
    elif sarezaru3==6:
        logozar7="⚅"

def zaru6calculator():
    global logozar8
    if sarezaru4==1:
            logozar8="⚀"
    elif sarezaru4==2:
            logozar8="⚁"
    elif sarezaru4==3:
            logozar8="⚂"
    elif sarezaru4==4:
            logozar8="⚃"
    elif sarezaru4==5:
            logozar8="⚄"
    elif sarezaru4==6:
            logozar8="⚅"

while True:
    if optiune == 1:
        #barbut la mai mica
        print("La mai mica")
        #jucator1 zar1
        zaru1jucator()
        zar1_jucator1 = sarezaru1
        #jucator1 zar2
        zar2_jucator1 = sarezaru2
        zaru2jucator()
        sum_zar_jucator1=zar1_jucator1+zar2_jucator1
        print("Ai dat:", logozar1, "+", logozar2," ", sum_zar_jucator1)
        #print("Ai dat:", sum_zar_jucator1)

        #calculator
        zar1_calculator =sarezaru3
        zaru1calculator()
        zar2_calculator = sarezaru4
        zaru2calculator()
        sum_zar_calculator=zar1_calculator+zar2_calculator
        print("Calculatorul a dat:", logozar3, "+", logozar4," ",sum_zar_calculator)

        #conditie castig
        if sum_zar_jucator1 < sum_zar_calculator:
            print("Ai castigat.")
        elif sum_zar_calculator == sum_zar_jucator1:
            print("Egalitate mai da o data")
        else:
            print ("Te-a facut calculatoru. N-ai talent la zaruri")
        break

    elif optiune == 2:
        #barbut la mai mare
        print("La mai mare")
        #jucator1
        zar1_jucator1 = sarezaru1
        zaru3jucator()

        zar2_jucator1 = sarezaru2
        zaru4jucator()
        
        sum_zar_jucator1=zar1_jucator1+zar2_jucator1
        print("Ai dat:",logozar5,"+",logozar6," ", sum_zar_jucator1)
        
        
        #calculator
        #zar1
        zar1_calculator =sarezaru3
        zaru5calculator()
        #zar2
        zar2_calculator = sarezaru4
        zaru6calculator()
        sum_zar_calculator=zar1_calculator+zar2_calculator
        print("Calculatoru a dat:", logozar7,"+", logozar8," ", sum_zar_calculator )
        
        
        #conditie castig
        if sum_zar_jucator1 > sum_zar_calculator:
            print("Ai castigat.")
        elif sum_zar_calculator == sum_zar_jucator1:
            print("Egalitate mai da o data")
        else:
            print ("Te-a facut calculatoru. N-ai talent la zaruri")
        break
    
    elif optiune != 1 and optiune !=2:
        print("Am inchis. Hai cu pacanelele 🂧🂧🂧")
        break


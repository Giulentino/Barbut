import random
optiune=int(input("⚀ La mai mica - apasa 1" "\n" "⚅ La mai mare - apasa 2" "\n:"))
#print ("Ai ales optiunea", optiune)
sarezaru1=random.randint(1, 6)
sarezaru2=random.randint(1, 6)
sarezaru3=sarezaru=random.randint(1, 6)
sarezaru4=sarezaru=random.randint(1, 6)


while True:
    if optiune == 1:
        #barbut la mai mica
        print("La mai mica")
        #jucator1
        zar1_jucator1 = sarezaru1
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
            ###
        zar2_jucator1 = sarezaru2
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
            ###
        sum_zar_jucator1=zar1_jucator1+zar2_jucator1
        #print("Ai dat:", sum_zar_jucator1,":",logozar1,zar1_jucator1, logozar2,zar2_jucator1)
        print("Ai dat:", logozar1, "+", logozar2," ", sum_zar_jucator1)

        #calculator
        zar1_calculator =sarezaru3
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
            ###
        zar2_calculator = sarezaru4
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
        sum_zar_calculator=zar1_calculator+zar2_calculator
        #print("Calculatoru a dat:", sum_zar_calculator, logozar3, zar1_calculator, logozar4, zar2_calculator)
        print("Calculatorul a dat:", logozar3, "+", logozar4," ",sum_zar_calculator)

        #conditie castig
        if sum_zar_jucator1 < sum_zar_calculator:
            print("Ai castigat.")
        elif sum_zar_calculator == sum_zar_jucator1:
            print("Egalitate mai da o data")
        else:
            print ("Te-a facut calculatoru.")
        break

    elif optiune == 2:
        #barbut la mai mare
        print("La mai mare")
        
        
        #jucator1
        zar1_jucator1 = sarezaru1
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

        zar2_jucator1 = sarezaru2
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
        sum_zar_jucator1=zar1_jucator1+zar2_jucator1
        print("Ai dat:",logozar1,"+",logozar2," ", sum_zar_jucator1)
        
        
        #calculator
        zar1_calculator =sarezaru3
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
        zar2_calculator = sarezaru4
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
        sum_zar_calculator=zar1_calculator+zar2_calculator
        #print("Calculatoru a dat:", , logozar3,zar1_calculator, logozar4, zar2_calculator)
        print("Calculatoru a dat:", logozar3,"+", logozar4," ", sum_zar_calculator )
        
        
        #conditie castig
        if sum_zar_jucator1 > sum_zar_calculator:
            print("Ai castigat.")
        elif sum_zar_calculator == sum_zar_jucator1:
            print("Egalitate mai da o data")
        else:
            print ("Te-a facut calculatoru.")
        break
    
    elif optiune != 1 and optiune !=2:
        print("Am inchis. Hai cu pacanelele 🂧🂧🂧")
        break


from calcolo_BMI import BMI



scelta = -1 

while(scelta != 0):
    print("-------------------------")
    print("[0]     Uscita")
    print()
    print("\n[1] Calcolo BMI ")
    print("\n[2] Calcolo BSA ")
    print("\n[3] Quanta acqua devo bere al giorno? ")

    scelta=int(input("Scegli: "))
    print("------------------------")
    print()
    if(scelta == 0):
        pass

    elif (scelta == 1):
        BMI(peso , altezza_m)


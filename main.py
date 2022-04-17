from calcolo_BMI import BMI
from calcolo_BSA import BSA
from check import check
##inserire peso e altezza
peso = float(input("Inserire peso in Kg: "))
altezza = float(input("Inserire altezza: "))
altezza_m = 0
altezza_cm = 0

altezza_m, altezza_cm = check(altezza, altezza_m, altezza_cm)

BSA(peso, altezza_cm)
BMI(peso, altezza_m)


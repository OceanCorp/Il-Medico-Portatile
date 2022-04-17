## CREAZIONE DI UN PROGRAMMA PER IL CALCOLO DEL BSA
## FORMULA BSA: ((altezza__in_centimetri * (peso / 3600)) ** 0.5)

def BSA(peso, altezza_cm):
    ## calcolo e stampa del  BSA
    BSA = ((altezza_cm * (peso / 3600)) ** 0.5) 
    print("BSA = %.3f" % BSA)
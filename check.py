## CONTROLLA IL TIPO DI ALTEZZA INSERITA E FA LE EVENTUALI CONVERSIONI
def check(altezza, altezza_m, altezza_cm, sesso):
    if (altezza > 3):
        altezza_m = altezza / 100
        altezza_cm = altezza
    else:
        altezza_cm = altezza * 100
        altezza_m = altezza

    if (sesso == "M"):
        sesso = 1

    elif (sesso == "F"):
        sesso = 0
    



    return altezza_m, altezza_cm, sesso



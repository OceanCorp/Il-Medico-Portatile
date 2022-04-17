def ideale(altezza_m , sesso):
    if sesso == 1:
        ideale = (altezza_m * altezza_m) * 22.1

    else:
        ideale = (altezza_m * altezza_m) * 20.26

    print("Il tuo peso ideale e' di: " , ideale , "Kg")



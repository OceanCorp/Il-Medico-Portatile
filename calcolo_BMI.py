## CREAZIONE DI UN PROGRAMMA PER IL CALCOLO DEL BMI
## FORMULA BMI: peso / (altezza_in_metri * altezza_in_metri)

def BMI(peso, altezza_m):
    ## calcolo e stampa del BMI
    BMI = peso / (altezza_m * altezza_m)
    print("BMI = %.2F" % BMI)

    ## definizione di una funzione per definire la valutazione dell'indice di massa corporea
    def valutazione(BMI):
        if (BMI < 16.5) :
            valutazione = "Sottopeso grave"
        elif (BMI <= 18.4) :
            valutazione = "Sottopeso"
        elif (BMI <= 24.9) :
            valutazione = "Normopeso"
        elif (BMI <= 30) :
            valutazione = "Sovrappeso"
        elif (BMI <= 34.9) :
            valutazione = "Obesita' di I grado"
        elif (BMI < 40) :
            valutazione = "Obesita' di II grado"
        else:
            valutazione = "Obesita' di III grado"
        
        print("Il tuo Indice di massa corporea riporta tale valutazione: ", valutazione)

    ## chiamata della funzione precedentemente definita per la valutazione dell'indice di massa corporea
    valutazione(BMI)
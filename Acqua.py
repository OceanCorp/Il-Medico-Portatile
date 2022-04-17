## FUNZIONE CHE CALCOLA I LITRI DI ACQUA MINIMI E MASSIMI DA BERE AL GIORNO

def acqua(peso):
    acqua_min = peso * 30
    acqua_max = peso * 50

    print("Devi bere minimo %.1f" % (acqua_min / 1000) , "L di acqua")
    print("Devi bere massimo %.1f" % (acqua_max / 1000) , "L di acqua")




palabra = input("Ingrese una palabra:")

palabra.lower()

def adecuar (x):

    lista = list(x)


    lista_final = []

    for letra in lista:
        if letra not in lista_final:
         lista_final.append(letra)

    
    lista_final.sort()
    
    return( lista_final)


print(adecuar(palabra))
 
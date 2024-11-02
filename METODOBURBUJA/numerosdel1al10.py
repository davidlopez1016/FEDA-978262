def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


numeros = [10, 2, 3, 8, 5, 6, 7, 1, 4, 9]


burbuja(numeros)

print("Lista ordenada:", numeros)

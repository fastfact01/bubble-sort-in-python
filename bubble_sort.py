
def bubblesort(lista):

    for n in range(len(lista)-1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


numeros = [7, 19, 1, 2, 13, 5, 23, 29, 11, 17, 6]
print(numeros)
bubblesort(numeros)
print(numeros)


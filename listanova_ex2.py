lista1 = []
lista2 = []
soma = []


def requestItems(lista1, lista2):
    print("Digite 5 números inteiros da primeira lista: ")
    for i in range(5):
        lista1.append(int(input("")))
    print("Digite 5 números inteiros da segunda lista: ")
    for i in range(5):
        lista2.append(int(input("")))
    return lista1, lista2


def somaListas(lista1, lista2, soma):
    print("Lista 1: ", lista1)
    print("Lista 2: ", lista2)
    for i in range(5):
        resultado = lista1[i] + lista2[i]
        soma.append(resultado)
    print("Soma: ", soma) 


requestItems(lista1, lista2)
somaListas(lista1, lista2, soma)
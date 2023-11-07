lista = [13, 41, 13, 8, 21, 7, 79]


def maiorElemento(lista):
    maior_elemento = lista[0]
    for elemento in lista:
        if elemento > maior_elemento:
            maior_elemento = elemento
    return maior_elemento


def menorElemento(lista):
    menor_elemento = lista[0]
    for elemento in lista:
        if elemento < menor_elemento:
            menor_elemento = elemento
    return menor_elemento


def num_ocorrencia(lista, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador  += 1
    return contador


print(lista)
numero = int(input("Digite o número a ser pesquisado na lista: "))
print("Maior elemento: ", maiorElemento(lista))
print("Menor elemento: ", menorElemento(lista))
print(f"Número de ocorrências do número {numero} na lista: ", num_ocorrencia(lista, numero))
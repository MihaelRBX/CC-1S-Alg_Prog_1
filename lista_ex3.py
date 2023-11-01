notas = []
def entradaNotas(notas):
    for i in range(1, 5):
        nota = float(input(f"Insira a nota {i}: "))
        while nota > 10 or nota < 0:
            nota = float(input(f"Valor fora do intervalo. Insira no vamente a nota {i}: "))
        notas.append(nota)
    return notas


def calculaMedia(notas):
    return sum(notas) / len(notas)


def imprimeNotaMedia(notas, calculaMedia):
    notas_string = ", ".join(map(str, notas))
    print("Notas: ", notas_string)
    media = calculaMedia(notas)
    print(f"Media das notas: {media:.2f}")


def main():
    entradaNotas(notas)
    calculaMedia(notas)
    imprimeNotaMedia(notas, calculaMedia)


main()

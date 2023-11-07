pesos = []
alturas = []

def entradaDados(pesos, alturas):
    for i in range(1, 16):
        pesos.append(float(input(f"Digite o peso da {i}° pessoa: ")))
        alturas.append(float(input(f"Digite a altura da {i}° pessoa: ")))
    return pesos, alturas


def saidaDados(pesos, alturas):
    for i in range(15):
        print(f"{i + 1}° pessoa: peso = {pesos[i]}, altura = {alturas[i]} e imc = {pesos[i] / (alturas[i]) ** 2:.2f}")


entradaDados(pesos, alturas)
saidaDados(pesos, alturas)
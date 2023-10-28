salarios = []

def lerSal(salarios):
    for i in range (1, 11):
        salarios.append(float(input(f"Insira o salario do funcionário {i}: ")))
    return salarios


def mediaSal(salarios):
    return sum(salarios) / len(salarios)


def maiorSal(salarios):
    maiorsalario = -9999
    for salario in salarios:
        if salario > maiorsalario:
            maiorsalario = salario
    print(f"Maior sálario: {maiorsalario}")


def salmenor850(salarios):
    contsalmenor850 = 0
    for salario in salarios:
        if salario < 850:
            contsalmenor850 += 1
    return contsalmenor850


def imprimeSal(salarios):
    for salario in salarios:
        print(salario)


def main():
    lerSal(salarios)
    imprimeSal(salarios)
    print(f"Média Salarial: {mediaSal(salarios)}")
    maiorSal(salarios)
    print(f"{salmenor850(salarios)} funcionários tiverem salário menor que R$850,00")


main()
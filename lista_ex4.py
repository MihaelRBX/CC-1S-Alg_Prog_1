vetor = []

def lerVetor(vetor):
    vetores = input("Insira o vetor: ")
    for i in vetores:
        vetor.append(i)    
    return vetor


def vogaisVetor(vetor):
    cont_vogal = 0
    for caracter in vetor:
        if caracter in ["a", "e", "i", "o", "u"]:
            cont_vogal += 1
    return cont_vogal



def consoantesVetor(vetor):
    cont_consoante = 0
    for caracter in vetor:
        if caracter not in ["a", "e", "i", "o", "u"]:
            cont_consoante += 1
    return cont_consoante


def imprimeDados(vetor, cont_vogal, cont_consoante):
    print("Vetor: ", "".join(vetor))
    print(f"Quantida de vogais: {cont_vogal}\nQuantidade de consoantes: {cont_consoante}")


lerVetor(vetor)
cont_vogal = vogaisVetor(vetor)
cont_consoante = consoantesVetor(vetor)
imprimeDados(vetor, cont_vogal, cont_consoante)
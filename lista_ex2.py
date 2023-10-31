vetores = []
def lerVetores(vetores):
  for i in range(1, 11):
    vetores.append(int(input(f"Insira o {i}° vetor: ")))
  return vetores


def inverteVetor(vetores):
  vetores.reverse()
  vetor_string = " ".join(map(str, vetores))
  print("Vetores invertidos: ", vetor_string)


lerVetores(vetores)
inverteVetor(vetores)
vetor = []

def entrada(vetor):
  for i in range(1, 7):
    vetor.append(int(input(f"Insira o {i}° número: ")))
  return vetor


def imprime(vetor):
  vetor_string = " ".join(map(str, vetor))
  print(vetor_string)


entrada(vetor)
imprime(vetor)
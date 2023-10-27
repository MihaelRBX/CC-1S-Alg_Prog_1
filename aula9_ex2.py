lista1 = []
lista2 = []
listacomum = []

for i in range(1, 6):
    lista1.append(int(input(f"Insira o {i}^ número da Primeira Lista: ")))

for i in range(1, 6):
    lista2.append(int(input(f"Insira o {i}^ número da Segunda Lista: ")))

comum = False

for a in lista1:
    for b in lista2:
        if (a == b):
            comum = True
            listacomum.append(a)

if not comum:
    print("Não existem elementos em comum.")
else:
    print("Números em comum: ", listacomum)

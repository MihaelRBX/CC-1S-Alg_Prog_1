#Faça um programa em Python que solicite ao usuário a placa e o valor da multa de 15 carros. As informações obtidas devem ser armazenadas em 2 listas distintas

placa = []
multa = []

for i in range(3):
    p = input("Placa: ")
    placa.append(p)
    m = float(input("Valor da Multa: "))
    multa.append(m)

media = sum(multa) / len(multa)

carros_multa300 = 0

for m in multa:
    if m >= 300:
        carros_multa300 += 1
    
print(media, carros_multa300)
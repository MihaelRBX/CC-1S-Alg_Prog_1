valores = []
par = []
impar = []

while True:
    num = int(input("Informe os valores: "))
    valores.append(num)
    escolha = input("Gostaria de continuar('S' para Sim e 'N' para não.)? ")
    if escolha.upper() == "S":
        continue
    break

for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f"Os valores são: {valores}\nOs valores pares são: {par}\nOs valores impar são: {impar}")

      

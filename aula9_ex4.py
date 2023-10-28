#Criar um programa em Python que leia o nome, a nota e curso (CC, ADS ou SI) de N alunos, cada informação deve ser armazenada em uma lista diferente. Observe que na posição i das três listas ficarão guardados: o nome do aluno i, a nota do aluno i e o curso do aluno i

nomes = []
notas = []
cursos = []
qtd_SI = 0
qtd_CC = 0
qtd_ADS = 0
soma_SI = 0
soma_CC = 0
soma_ADS = 0

resp = 's'
while resp.upper() ==  "S":
    nome = input("Digite o nome do aluno: ")
    nomes.append(nome)
    curso = input("Digite o nome do curso: ")
    cursos.append(curso)
    nota = float(input("Digite a nota do aluno:"))
    notas.append(nota)
    if curso.upper() == "CC":
        qtd_CC += 1
        soma_CC += nota
    elif curso.upper() == "ADS":
        qtd_ADS += 1
        soma_ADS += nota
    else:
        qtd_SI += 1
        soma_SI += nota
    print()
    resp = input("Deseja adicionar outro aluno?")

media_CC = soma_CC / qtd_CC
media_SI = soma_SI / qtd_SI
media_ADS = soma_ADS / qtd_ADS
print(f"Médias: \nCC:{media_CC}\nSI:{media_SI}\nADS:{media_ADS}")

acima_mediaCC = 0
acima_mediaSI = 0
acima_mediaADS = 0

for i in range(len(notas)):
    if cursos[i] == "CC" and notas[i] > media_CC:
        acima_mediaCC += 1
    elif cursos[i] == "SI" and notas[i] > media_SI:
        acima_mediaSI += 1
    elif cursos[i] == "ADS" and notas[i] > media_ADS:
        acima_mediaADS += 1

print(f"Alunos acima da média: \nCC: {acima_mediaCC}\nSI: {acima_mediaSI}\nADS: {acima_mediaADS}")
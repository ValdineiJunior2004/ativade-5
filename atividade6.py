
alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

# calcula a média das notas
soma_notas = sum(alunos.values())
media_notas = soma_notas / len(alunos)

# exibe a média
print("A média das notas é:", media_notas)

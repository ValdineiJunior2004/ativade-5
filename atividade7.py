
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento


print("A soma de todos os elementos da matriz é:", soma)

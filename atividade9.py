def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em Km/h): "))
    return tempo, velocidade


def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia


def calcular_litros(distancia):
    litros = distancia / 12
    return litros


def apresentar_resultado(velocidade, tempo, distancia, litros):
    print(f"Velocidade média: {velocidade} Km/h")
    print(f"Tempo gasto na viagem: {tempo} horas")
    print(f"Distância percorrida: {distancia} Km")
    print(f"Quantidade de litros utilizada: {litros:.2f} litros")

def main():
    tempo, velocidade = ler_valores()
    distancia = calcular_distancia(tempo, velocidade)
    litros = calcular_litros(distancia)
    apresentar_resultado(velocidade, tempo, distancia, litros)

if __name__ == "__main__":
    main()

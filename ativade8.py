def ler_temperatura():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    return celsius


def converter_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit


def mostrar_resultado(fahrenheit):
    print("A temperatura em graus Fahrenheit é:", fahrenheit)

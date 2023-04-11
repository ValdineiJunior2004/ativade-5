def calcular_media(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    return media

lista_exemplo = [10, 20, 30, 40, 50]
media_lista = calcular_media(lista_exemplo)
print("A média da lista é:", media_lista)

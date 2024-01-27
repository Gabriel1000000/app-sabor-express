# Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
calculo = [10,20,30,40,50]
media=0
soma=0
try:
    for num in calculo:
        soma+=num
    media=len(calculo)
    resultado=soma/media
    print(f'Resultado da média é de {resultado},{media}')
except Exception as erro:
    print(f'Ocorreu um erro: {erro}')
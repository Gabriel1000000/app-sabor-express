# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
calculo = [10,20,30,40,50]
soma_num=0
try:
    for cont in calculo:
        soma_num+=cont
    print(f'Os números somados forem esses: {calculo}')
    print(f'O resultado da soma foi esse: {soma_num}')

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
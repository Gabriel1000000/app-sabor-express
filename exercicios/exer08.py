# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

num_decresente = []
try:
    for num in range(10, 0, -1):
        num_decresente.append(num)
    print(num_decresente)
except:
    print('erro!')
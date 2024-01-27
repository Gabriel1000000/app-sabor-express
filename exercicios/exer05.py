# Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

num_list = [] 
nome_list = []
num_ano=[]

try:
    for num in range(1, 11):
        num_list.append(num)
    print(num_list)
    for nome in range(4):
        nome_list.append(input('Informe um nome: '))
        faltam=4-nome
        print(f'Nome guardado com sucesso, faltam {faltam} de 4')
    print(f'Os nomes salvos são: {nome_list}')
    for ano in range(2000, 2024):
        num_ano.append(ano)
    print(num_ano)
except:
    print('erro!')
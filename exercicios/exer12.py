#  Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

import os

cadastro_de_aluno =[
    {'nome':'Gabriel', 'idade':23, 'cidade':'Rio de Janeiro'},
    {'nome':'Miko', 'idade':20, 'cidade':'Rio de Janeiro'}
]

def main():
    exibir_opcao()

def exibir_opcao():
    print('============Escola python para todos============')
    print('Selecione [1] para ver os alunos cadastrados.')
    print('Selecione [2] para cadastrar um aluno.')
    print('Selecione [3] para saie no menu da escola.')
    opcao_escolhida()

def opcao_escolhida():
    try:
        opcao = int(input('Informe sua escolha: '))

        match opcao:
            case 1:
                exibir_lista_aluno()
            case 2:
                cadastrado_aluno()
            case 3:
                fechar_progama()       

    except Exception as erro:
        print(f'Informaçõe sobre o erro: {erro}' )

def exibir_lista_aluno():
    for aluno in cadastro_de_aluno:
        nome=aluno['nome']
        idade=aluno['idade']
        cidade=aluno['cidade']
        print(f'Nome: {nome.ljust(7)} | Idade: {idade} | Cidade: {cidade}')
    voltar_ao_menu()

def cadastrado_aluno():
    novo_aluno=input('Informe o nome do novo aluno: ')
    idade=int(input(f'Informe a idade do aluno {novo_aluno}: '))
    cidade=input(f'Informe a cidade do aluno {novo_aluno}: ')
    novos_dados={'nome':novo_aluno, 'idade':idade, 'cidade':cidade}
    cadastro_de_aluno.append(novos_dados)
    voltar_ao_menu()

def fechar_progama():
    os.system('cls')
    print('Obridado por escolher nossa escola!')

def voltar_ao_menu():
    input('Aperte enter para voltar ao menu: ')
    main()

if __name__ == '__main__':
    main()

import os

restaurantes = []

def exibir_nome_do_programa():
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    # print('Sabor-Express!\n')

def exibir_opcao(): 
    print('1. Cadastro de restaurante')
    print('2. Listar restalrantes')
    print('3. Ativar restalrante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'======================{texto}======================')

def encerrando_programa():
    os.system('cls')
    print('Progama encerrado!')
    print('Obrigao por usa o nosso app!')

def voltar_ao_menu():
    input('Digite qualquer tecla para continuar: ')
    main()

def opcao_invalida():
    print('Opção em valida!')
    voltar_ao_menu()

def cadastro_novo_restaurantes():
    exibir_subtitulo('Cadastro de restaurante')
    nome_restaurantes = input('Informe o nome do restaurante: ')
    restaurantes.append(nome_restaurantes)
    print(f'O restaurante {nome_restaurantes} foi cadatrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')
    for restaurante in restaurantes:

        print(f'.{restaurante}')
    
    voltar_ao_menu()

def escolher_opcao():
    # usei o "try" para fazer a verificação, se o valor dado pelo usuario é valido, então funciona normalmente, mas se o valor for diferente dos que estão no "if" a função "except" chama a função de "opcao_invalida()".
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastro_novo_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante!')
        elif opcao_escolhida == 4:
            encerrando_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()



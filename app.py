import os

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

def encerrando_programa():
    os.system('cls')
    print('Progama encerrado!')
    print('Obrigao por usa o nosso app!')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        print('Cadastro de restaurante!')
    elif opcao_escolhida == 2:
        print('Listar restaurantes!')
    elif opcao_escolhida == 3:
        print('Ativar restaurante!')
    else:
        encerrando_programa()

def main():
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()



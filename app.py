import os

restaurantes = [{'nome':'Zé da pança', 'categoria':'churrasco', 'ativo':True},
                {'nome':'Saude vegana', 'categoria':'vegano', 'ativo':False}
]

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
    print('3. Ativar status do restalrante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*'*(len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)

def encerrando_programa():
    os.system('cls')
    print('Progama encerrado!')
    print('Obrigao por usa o nosso app!')

def voltar_ao_menu():
    input('Digite qualquer tecla para continuar: ')
    main()

def opcao_invalida(texto):
    print('Opção em valida!')
    print(f'Mais detalhes do erro: {texto}')
    voltar_ao_menu()

def cadastro_novo_restaurantes():
    exibir_subtitulo(' Cadastro de restaurante ')
    nome_restaurantes = input('Informe o nome do restaurante: ')
    categoria = input(f'Informe a categoria do restaurante {nome_restaurantes}: ')
    dados_do_restaurante = {'nome':nome_restaurantes,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurantes} foi cadatrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo(' Lista de restaurantes ')
    print(f'{"Nome dos restaurantes".ljust(26)} | {"Categoria".ljust(31)} | {"Status"} ')
    for restaurante in restaurantes: 
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativo' if restaurante['ativo'] else 'Desativado'
            print(f'Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria.ljust(20)} | Status: {ativo}')
    
    voltar_ao_menu()

def alterar_status():
    exibir_subtitulo(' Alterando o status do restaurante ')
    nome_restaurante = input('Informe o nome do restaurante deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('Resturante não encontrado!')   

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
            alterar_status()
        elif opcao_escolhida == 4:
            encerrando_programa()
        else:
            opcao_invalida()
    except Exception as erro:
        opcao_invalida(erro)

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()

# Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
import os 

funcionarios=[{'nome':'Gabriel', 'idade':24, 'profição':'desenvolvedor junior'},
              {'nome':'GB', 'idade':24, 'profição':'estágiario'}
             ]

def mostrar():
    apresentacao('Lista dos funcionarios cadastrado ')
    for funcionario in funcionarios:
        nomes_dos_funcionarios=funcionario['nome']
        idades_dos_funcionarios=funcionario['idade']
        proficoes_do_funcionarios=funcionario['profição']
        print(f'Nome: {nomes_dos_funcionarios.ljust(20)} | Idade: {idades_dos_funcionarios} | Profição: {proficoes_do_funcionarios}')
    voltar_ao_menu()

def menu_modificacao():
    apresentacao(' Menu de modificação ')
    print('Opções de modificação de dados do funcionario')
    print('Para alterar o nome digite [1]')
    print('Para alterar a idade digite [2]')
    print('Para alterar a profição digite [3]')
    print('Para voltar ao menu [4]')
    print('Para sair do programa digite [5]')

def opcao_escolhida_modificacao(nome_funcionario):
    try:
        opcao_modificar=int(input('Informe uma opção: '))
        match opcao_modificar:
            case 1:
                modificacao_nome(nome_funcionario)
            case 2:
                modificacao_idade(nome_funcionario)
            case 3:
                modificar_proficao(nome_funcionario)
            case 4:
                voltar_ao_menu()
            case 5:
                print('saindo')

    except Exception as erro:
        opcao_invalida(erro)

def modificacao_nome(nome_funcionario):
    novo_nome=input('Inoforme o novo nome do funcionario: ')
    for cadastrado in funcionarios:
        if nome_funcionario == cadastrado['nome']:
            cadastrado['nome']=novo_nome
    continuar_modificando(nome_funcionario)

def modificacao_idade(nome_funcionario):
    nova_idade=input('Informe a idade do funcionario: ')
    for funcionario in funcionarios:
        if nome_funcionario == funcionario['nome']:
            funcionario['idade']=nova_idade
    continuar_modificando(nome_funcionario)

def modificar_proficao(nome_funcionario):
    nova_proficao=input(f'Informe a nova profição do funciomario, {nome_funcionario}')
    for proficao in funcionarios:
        if nome_funcionario == proficao['nome']:
            proficao['profição']=nova_proficao
    continuar_modificando(nome_funcionario)

def modificacao():
    buscar_nome=input('Informe o nome do funcionario que deseja modificar os dados: ')
    for nome in funcionarios:
        if buscar_nome == nome['nome']:
            menu_modificacao()
            opcao_escolhida_modificacao(buscar_nome)
    
def continuar_modificando(nome_funcionario):
    os.system('cls')
    apresentacao(' Continar a modificar? ')
    print('Para continuar modificando digite [1]')
    print('Para voltar ao menu principal digite [2]')
    continua= int(input('Informe uma das opções: '))
    if continua == 1:
        menu_modificacao()
        opcao_escolhida_modificacao(nome_funcionario)
    elif continua == 2:
        voltar_ao_menu()
    else:
        print('ERRO!')


def adicionar():
    apresentacao(' Cadastro de um funcionario novo ')
    nome_cadastro=input('Informe o nome do novo funcionario: ')
    idade_cadatro=int(input(f'Informe a idade do {nome_cadastro} : '))
    proficao_cadastro=input(f'Infroem a profição do {nome_cadastro}: ')
    dados_para_cadastro={'nome':nome_cadastro, 'idade':idade_cadatro, 'profição':proficao_cadastro}
    funcionarios.append(dados_para_cadastro)
    print(f'O funcionario {nome_cadastro} foi cadastrado com sucesso!')
    voltar_ao_menu()
    

def remover():
    apresentacao(' Remoção de um funcionario ')
    nome_removido=input('informe o nome do funcionario que vai ser removido: ')
    funcionario_encontrado=False
    for removido in funcionarios:
        if nome_removido == removido['nome']:
          funcionarios.remove(removido)
          funcionario_encontrado=True
    if funcionario_encontrado:
        print('Funcionario removido com sucesso!')
    else:
        print('Funcionario não encontrado')
    voltar_ao_menu()

def apresentacao(texto):
    os.system('cls')
    linha='*'*len(texto)
    print(linha)
    print(texto)
    print(linha)

def opcao():
    apresentacao(' Bem vindo a empresa python loko ')
    print('Escolha a opção')
    print('Para ver os funcionarios selecione[1]')
    print('Para modificar os dados de um funcionarios selecione[2]')
    print('Para adicionar um funcionario selecione[3]')
    print('Para remover um funcionario selecione[4]')
    print('Para sair no menu selecione[5]')

def voltar_ao_menu():
    input('Digite qualquer tecla para continuar: ')
    main()

def opcao_invalida(texto):
    print(f'Mais detalhe sobre o erro{texto}')

def opcao_escolhida():
    try:
        opcao=int(input('Informe uma opção: '))
        match opcao:
            case 1:
                mostrar()
            case 2:
                modificacao()
            case 3:
                adicionar()
            case 4:
                remover()
            case 5:
                print('saindo')

    except Exception as erro:
        opcao_invalida(erro)

def main():
    os.system('cls')
    opcao()
    opcao_escolhida()

if __name__ == '__main__':
    main()
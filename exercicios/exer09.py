# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.


def tabuada_especifica():
    num = int(input('Informe um número para fazer a tabuada: '))
    for tabuada in range(11):
        resultado= num*tabuada
        print(f'{num} X {tabuada} = {resultado}')

def tabuada_total():
    for num in range(11):
        print(f'=================Tabuada de {num}===============================')
        for tabuada in range(11):
            res = num*tabuada    
            print(f'{num}X{tabuada}={res}')

def main():
    opcao_escolida()



try:
    def opcao_escolida():
        print('==========Bem-vindo ao criado de tabuada==========')
        print('Para criar uma tabuada especifica digite [1]')
        print('Para criar uma tabuada de 0 a 10 digite [2]')
        opcao=int(input('Qual opção você deseja: '))
        match opcao:
            case 1:
                tabuada_especifica()
            case 2:
                tabuada_total()
except Exception as erro:
    print('erro!')
    print(f'Detalhes do erro: {erro}')


if __name__ == '__main__':
    main()
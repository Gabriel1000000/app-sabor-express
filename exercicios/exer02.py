# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print('****Ben-vindo ao classificador de idade!*****\n')
idade = int(input('Informe a idade para a classificação: '))

if idade == 0 or idade <=12:
    print('A calssificação é uma Criança!')
elif idade == 13 or idade <= 18:
    print('A calssificação é uma Adolescente!')
elif idade > 18:
    print('A calssificação é uma Adulto!')
else:
    print('Informe a idade valida!')
    
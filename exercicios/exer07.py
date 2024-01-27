# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
num_par = []

try:
    for num in range(1,11):
        if num%2 == 0:
            num_par.append(num)
        else: 
            soma=num+num
            
    print(f'A soma dos número ímpares de 1 até 10 são {soma}')
    print(f'Os número de 1 até 10 que são pares {num_par}')
except:
    print('erro!')
# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

print('=========Log de entrada=========')
user = input('Usuario: ')
senha = input('Senha: ')
if user == "gavar" and senha == "123@":
    print('Usuario e senha validos!')
    print('Acesso permitido!')
else:    
    print('*****!!!!*****')
    print('ACESSO NEGADO!')
    print('*****!!!!*****')
    

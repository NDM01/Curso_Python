utilizador = input('Insira o seu nome: ')
senha = input('Insira a senha: ')

utilizador_bd = 'Daniel'
senha_bd = '12345'

if utilizador == utilizador_bd and senha == senha_bd:
    print("Login efetuado com sucesso!")
else:
    print("Oops algum dado introduzido incorreto!")
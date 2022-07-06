"""
Os temas abordados nesta aula são o IF, ELIF e ELSE
"""
nome = input("Insira o seu nome: ")
idade = int(input("Insira a sua idade: "))
e_maior = idade >= 18

if e_maior is True:
    print(f'O seu nome é {nome} e é maior de idade')
elif e_maior is False:
    print(f'O seu nome é {nome} e é menor de idade')

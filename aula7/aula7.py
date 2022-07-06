"""
Nesta aula o tema abordado é a introdução a formatação de strings
"""
nome = 'Daniel França'  # str
idade = 18  # int
altura = 1.70  # float
e_maior = idade > 18  # bool
peso = 71  # int
imc = peso / (altura ** 2)

print(nome, 'tem', idade, ' anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e o seu imc é {imc:.2f}')
print("{} tem {} anos de idade e o seu imc é {:.2f}".format(nome, idade, imc))
print("{n} tem {i} anos de idade e o seu imc é {im:.2f}".format(n=nome,i=idade,im=imc))

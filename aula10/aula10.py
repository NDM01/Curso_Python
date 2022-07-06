"""
Nesta aula os temas abordados serão os operadores relacionais
==  igualdade
<   menor que
<=  menor ou igual a
>   maior que
>=  maior ou igual a
!=  diferente
"""
nome = input('Insira o seu nome: ')
idade = int(input('Insira a sua idade: '))

# Idade mínima para pedir empréstimo
idade_minima = 18

if idade < 18:
    print('Idade inválida!')
else:
    print("Aceite")

"""
Nesta aula é abordado a Formatação de valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(Quantidade)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'Daniel Franca'
print(f'{nome:#^30}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

nome = nome.ljust(20, '#')
print(nome)

print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas

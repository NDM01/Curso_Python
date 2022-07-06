"""
O tema abordado nesta aula são:
Funções - def em Python (Parte 1)

"""


def saudacao(msg='Olá', nome='utilizador'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()

print(variavel)
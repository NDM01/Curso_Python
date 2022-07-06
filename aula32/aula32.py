"""
O tema abordado nesta aula são:
Funções - def em Python - *args **kwargs -(Parte 3)

print(*lista) - Mostra a lista sem os []
"""


def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Daniel', sobrenome='Franca', idade=18)

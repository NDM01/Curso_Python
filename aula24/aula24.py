"""
* Enumerate - Enumerar elementos da lista # list
"""
lista = [
    ['Daniel', 'Maria', 'Afonso'],
    ['Eduardo', 'Pedro', 'Tiago'],
    ['Hugo', 'João', 'Carlos'],
]

for v1 in enumerate(lista, 1):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
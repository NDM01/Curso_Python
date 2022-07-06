"""
Nesta aula o tema abordado é:
Try e except como condicional
"""

def converter_valor(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converter_valor(input('Insira um número: '))

    if numero is None:
        print('Erro: Isto não é um número!')
    else:
        print(numero * 2)
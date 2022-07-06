"""
Nesta aula o tema abordado é:
Try, Except - Exceções em Python
"""

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro!')
except NameError as erro:
    print('Erro de desenvolvedor')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    a = ''
print(a)
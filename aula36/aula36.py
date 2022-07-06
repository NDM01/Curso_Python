"""
O tem abordado nesta aula é:
Dicionário
"""

clientes = {
    'cliente1': {
        'nome': 'Daniel',
        'sobrenome': 'Franca',
    },
    'cliente2': {
        'nome': 'Maria',
        'sobrenome': 'Clara'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'A mostrar {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

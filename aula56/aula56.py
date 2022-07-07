"""
Nesta aula o tema abordado é:
Como criar pacotes e módulos no Python
"""

from Vendas.cacl_prec import aumento, reduzir
from Vendas.format.preco import format

preco = 49.90
preco_com_aumento = aumento(valor=preco, percentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reduzir(valor=preco, percentagem=15, formata=True)
print(preco_com_reducao)


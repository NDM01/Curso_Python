"""
Nesta aula o tem abordado são:
Geradores, Iteradores e Iteráveis
"""
import sys

l1 = [x for x in range(100000)]  #lista
l2 = (x for x in range(100000))  #dicionário

# for v in l2:
#   print(v)


print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

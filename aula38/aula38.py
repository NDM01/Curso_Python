"""
Nesta aula o tema abordado é:

add (adicional), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

"""
l1 = ['Daniel', 'João', ' Afonso']
l2 = ['Maria', 'Daniel', 'Nelson',
      'Daniel', 'Daniel', 'Daniel', 'Daniel', 'Daniel', 'Daniel']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')
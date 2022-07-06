"""
Nesta aula os temas abordados são o While / Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador,acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei ao else')  # Este else não é executado pois tem um break
print('Isto está a ser executado')
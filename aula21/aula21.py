"""
Nesta aula o tema abordado é:
Listas em Python
Append, insert, pop, del, clear, extend, +
Min, Max
Range
"""
secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Perdeu!!')
        break

    letra = input('Insira uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns acertou na palavra! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Chances disponíveis: {chances}')
    print()
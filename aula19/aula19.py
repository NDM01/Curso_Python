"""
Nesta aula o tema abordado é strings com while
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_utilizador = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_utilizador:
        nova_string += input_utilizador.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

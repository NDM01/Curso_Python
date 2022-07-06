"""
Nesta aula os temas abordados são operadores lógicos
and
or
not
in
not in
"""
a = 2
b = 3
c = ''

# IF Normal
if b > a:
    print("B é maior do que A")
else:
    print("A é maior que B")

# IF com not
if not b > a:
    print("B é maior do que A")
else:
    print("A é maior que B")

# IF que verifica se variável tem algum valor atribuido
if not c:
    print('Por favor, preencha o valor de C')

# IF que verifica se no nome contém o caracter a
nome = input("Insira o seu nome: ")
if 'a' in nome:
    print("Existe a letra a no seu nome")

# IF que verifica se no valor não contem o caracter
animal = input("Insira o seu animal favorito: ")
if 'a' not in animal:
    print("O seu animal não contém a letra 'a'!")

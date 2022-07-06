"""
Nesta aula o tema abordado é a entrada de dados
"""
nome = input("Insira o nome: ")
idade = input("Insira a idade: ")
ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')

# As duas maneiras de tornar uma str em int
num1 = int(input("Insira o primeiro número: "))
num2 = input("Insira o segundo número: ")
num2 = int(num2)

print(num1 + num2)


"""
Nesta aula o tema abordado será o while
Utilizado para realizar ações enquanto uma condição
for verdadeira
"""
while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair?\n[S]Sim ou [N]Não")

    if sair == 'S':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Número inválido")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print("Operador inválido")

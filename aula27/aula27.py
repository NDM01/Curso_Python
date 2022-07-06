"""
O tema abordado nesta aula é o Operador ternário em Python
"""
idade = input("Insira a sua idade: ")

if not idade.isnumeric():
    print("Insira apenas números")
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode entrar' if e_maior else 'Não pode entrar'

print(msg)
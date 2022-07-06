"""
Nesta aula o tema abordado é a documentação e funções built-in
"""
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')

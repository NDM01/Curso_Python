"""
Nesta aula serão abordados os tipos de dados:
str - string -> textos 'Assim' "Assim"
int - inteiro -> 123456.. 0 -10 -20 -50...
float - real/ponto flutuante (número com casas décimais) -> 10.50 1.5 -50.93
bool - booleano/lógico -> True/False
"""
# O type mostra se o valor é str ou int ou etc

print('Daniel', type('Daniel'))

print(100, type(100))

print(1.07, type(1.07))

print(10 == 10, type(10 == 10))

print('Daniel' == 'Daniel', type('Daniel' == 'Daniel'))

print('Daniel' == 'daniel', type('Daniel' == 'daniel'))

print(bool(1 == 4))

print('Daniel', type('Daniel'), bool('Daniel'))

print('10', type('10'), type(int('10')))

print(10 + 10)

print('10' + '10')

# String: nome
print('Daniel', type('Daniel'))

# Idade: int
print(18, type(18))

# Altura: float
print(1.77, type(1.77))

# É maior de idade: bool
print(bool(18 >= 18))

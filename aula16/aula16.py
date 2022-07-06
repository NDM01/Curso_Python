"""
Nesta aula o tema abordado será a manipulação de strings
- String indices
- Remoção de strings [inicio:fim:passo]
- Funções built-in len, abs, type, print, etc...
Estas funções podem ser usadas diretamente em cada tipo.

Podemos conferir aqui:
 https://docs.pyhon.org/3/library/stdtypes.html (tipos built-in)
 https://docs.python.org/3/library/functions.html (funções built-in)
"""
# Positivos  [012345678]
texto       ='Python s2'  # Isto é um exemplo para entender, NÃO FAZER ASSIM!
# Negativos -[987654321]

url = "www.google.com.pt/"

print(url[:-1])  # Remove as strings que pretendermos

nova_string = texto[:6]
nova_string2 = texto[0:6:2]
print(nova_string2)
print(nova_string)
print(texto[8])

print( len(texto))

for letra in texto:
    print(letra)
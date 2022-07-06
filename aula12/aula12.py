"""
Nesta aula o tema abordado é a quantidade de caracteres
"""
string1 = input("Insira a primeira palavra: ")
string2 = input("Insira a segunda palavra: ")

print(f'A quantidade total de caracteres é {len(string1) + len(string2)}')

print(len(string2))
# OU
print((string2.__len__()))
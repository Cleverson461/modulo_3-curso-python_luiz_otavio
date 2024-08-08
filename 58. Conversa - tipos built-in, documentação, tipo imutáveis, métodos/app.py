"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: str, int, float, bool
"""

string = '1000'
#string = 'Cléverson'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
# outra_variavel = string
# print(string)
print(outra_variavel)

print(string.zfill(10))
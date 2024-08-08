"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""



#          +01234
#          -54321
string = 'ABCDE' # 5 caracteres (len)
# lista = [] # " "
# print(bool([])) # falsy
# print(lista, type(lista))

#         0     1       2           3    4
#        -5    -4      -3          -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[2] = 'Cléverson'
print(lista[2].upper(), type(lista[2]))
print(lista[-3])
print(lista)
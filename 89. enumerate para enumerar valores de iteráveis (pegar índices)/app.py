"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# for item in enumerate(lista):
#     a, b = item
#     print(f'Item: {a}, Valor: {b}')

for tupla_enumerada in enumerate(lista):
    print(f'FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\tValor: {valor}')

# lista_enumerada = list(enumerate(lista, start=10))

# print(lista_enumerada)
#print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)
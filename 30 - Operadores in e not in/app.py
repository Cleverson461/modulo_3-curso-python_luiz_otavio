# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 
#  o t a v i o 
# -6-5-4-3-2-1

# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])

""" print('á' in nome)
print('vio' in nome)
print(10 * '-')

print('vio' not in nome)
print('zero' not in nome)
print(10 * '-')

print('z' in nome)
print('0' in nome) """

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
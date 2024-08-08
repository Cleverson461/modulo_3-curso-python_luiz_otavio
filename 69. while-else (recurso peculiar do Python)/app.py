""" while/else """
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break  # Interrompe o laço e pula para o else
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
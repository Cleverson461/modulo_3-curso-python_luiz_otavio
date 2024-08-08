""" frase = 'aaaoooo'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    
    # print(letra_atual, qtd_vezes_letra_apareceu)
    i += 1
print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu {qtd_atual}x') """

start = 0
end = 10
while start < end:
    start += 1
    print(start)
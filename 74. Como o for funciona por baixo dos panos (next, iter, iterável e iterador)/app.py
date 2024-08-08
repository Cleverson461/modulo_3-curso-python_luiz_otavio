"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Cléverson' # iterável

""" iterador = iter(texto) # iterator
while True:
    try:
        letra = next(iterador)
        print(letra) # me entrega o próximo valor
    except StopIteration:
        break # sai do loop caso não haja mais valores """

for letra in texto:
    print(f'Passou no {letra}.')
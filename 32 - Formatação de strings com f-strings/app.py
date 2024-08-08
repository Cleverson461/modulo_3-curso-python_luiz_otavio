""" 
    Formatação básica de strings
    s - string
    d e i - int
    f - float
    .<números de dígitos>f
    x e X - Hexadecimal (ABCDEF0123456789)
    (Caractere)(><^)(quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    = - Força o número a aparecer antes dos zeros
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a

"""
variaval = 'ABC'
print(f'{variaval}')
print(f'{variaval: >10}')
print(f'{variaval: <10}.')
print(f'{variaval: ^10}.')
print(f'{variaval:0^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:04X}')
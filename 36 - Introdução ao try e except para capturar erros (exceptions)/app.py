""" 
    Introdução ao try/except
    try -> tentar executar o código
    except -> caso o código falhe, executar esse bloco de código (OCORREU ALGUM ERRO AO TENTAR EXECUTAR)
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    #print('STR:', numero_str)
    numero_float = float(numero_str)
    
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    print(f'Isso não é um número válido. Por favor, digite um número.')


""" if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print(f'Isso não é um número') """
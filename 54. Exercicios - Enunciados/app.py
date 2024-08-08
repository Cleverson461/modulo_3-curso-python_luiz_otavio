"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_int = input('Digite um numero inteiro: ')
# inteiro_numero = int(numero_int)

# if inteiro_numero % 2 == 0:
#     print(f'O {inteiro_numero} é par')
# elif inteiro_numero % 2 == 1:
#     print(f'O {inteiro_numero} é ímpar')
# else:
#     print(f'O {inteiro_numero} não é um número inteiro')
    
"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite a hora em números em inteiros: ')
# inteira_hora = int(hora)

# if inteira_hora >= 6 and inteira_hora <= 11:
#     print(f'Bom dia, é {inteira_hora:.2f} agora.')
# elif inteira_hora >= 12 and inteira_hora <= 17:
#     print(f'Boa tarde, é {inteira_hora:.2f} agora')
# elif inteira_hora >= 18 and inteira_hora <= 23:
#     print(f'Boa noite, é {inteira_hora:.2f} agora')
# else:
#     print('Boa madrugada')

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
  if tamanho_nome <= 4:
    print('Seu nome é curto')
  elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
  else:
    print('Seu nome é muito grande')
else:
  print('Por favor, digite alguma coisa.')
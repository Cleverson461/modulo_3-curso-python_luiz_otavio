primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)

if int_primeiro > int_segundo:
    print(f'O primeiro_valor={int_primeiro} é maior que o segundo_valor={int_segundo}')
elif int_segundo > int_primeiro:
    print(f'O segundo_valor={int_segundo} é maior que o primeiro_valor={int_primeiro}')
else:
    print(f'Os valores são iguais')
    
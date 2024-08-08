# Operadores lógicos
# or (ou) 
# or - Qualuqer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy(que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um nào valor

""" entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
# if condição(for True(verdadeira))
#   ...

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou no aplicativo com sucesso!')
else:
    print('Sair') """

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
print(True or 0 or True)
print(bool(''))
print(bool(0.0))
print(bool(0))
# senha = (0 or False or 0 or 'abc')
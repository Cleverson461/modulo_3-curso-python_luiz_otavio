"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
          indice = int(indice_str)
          del lista[indice]
          print('Valor apagado com sucesso.')
        except ValueError:
          print('Não foi possível apagar esse índice.')
        except IndexError:
          print('Não foi possível apagar esse índice.')
        except Exception:
            print('Ocorreu um erro inesperado.')
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print('Sua lista está vazia.')
        
        for i, valor in enumerate(lista):
            print(f'{i}. {valor}')
        
    else:
        print('Opção inválida. Escolha i, a ou l. Tente novamente.')

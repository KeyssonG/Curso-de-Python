"""
Faça uma lista de compras com listas 
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de índices
inexistentes na lista. 
"""
"""
# resposta alternativa
lista_de_compras = []

def mostrar_menu():
    print("===== Lista de Compras =====")
    print("1 - Adicionar item a lista")
    print("2 - Remover item da lista")
    print("3 - Listar itens da lista")
    print("0 - Sair")

def adicionar_item():
    item = input("Digite o item que deseja adicionar: ")
    lista_de_compras.append(item)
    print(f"{item} foi adicionado a lista!")

def remover_item():
    if len(lista_de_compras) == 0:
        print("A lista de compras está vazia!")
        return

    print("Itens na lista de compras:")
    for i, item in enumerate(lista_de_compras):
        print(f"{i} - {item}")

    try:
        indice = input("Digite o número do item que deseja remover: ")
        item_removido = lista_de_compras.pop(indice)
        print(f"{item_removido} foi removido da lista!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
    except IndexError:
        print("Indice inválido! Por favor, insira um número válido.")

def listar_itens():
    if len(lista_de_compras) == 0:
        print("A lista de compras está vazia!")
        return

    print("Itens na lista de compras:")
    for i, item in enumerate(lista_de_compras):
        print(f"{i} - {item}")

while True:
    mostrar_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        remover_item()
    elif opcao == "3":
        listar_itens()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")            


# Resposta do curso
"""
import os 

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        #os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )    

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        #os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')



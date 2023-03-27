"""
Exercício 
Peça ao usuário para digitar seu nome
peça ao usuário para digitar a sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome intervido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {Letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você ainda deixou campos vazios."        
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f' Seu nome é {nome}')
    print(f'Seu nome intervido é {nome[::-1]}')
   
    if ' ' in nome:
        print('Seu nome contém (ou não) espaços')

    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')    
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print("Desculpe, você ainda deixou campos vazios.")
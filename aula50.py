"""

Exercício
Exiba os índices da lista
0 Maria
1 helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type[indice])
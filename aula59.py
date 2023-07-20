# Desempacotamento em chamadas
# de métodos e funções 
string = 'ABCD'
lista = [ 'Maria', 'helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [

    # 0        1
    ['Maria', 'helena',], #2

    # 0
    ['Elaine',], #1
    #0        1       2
    ['Luiz', 'João', 'Eduarda', ], #2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
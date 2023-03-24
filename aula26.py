"""
Interpolação básica de strings
 s - string
 d e i - int
 f - float
 .<número de dígitos>f
 x ou x Hexadecimal
 (Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 Sinal - + ou -
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08x}')
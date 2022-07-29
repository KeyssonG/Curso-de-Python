from numbers import Real


real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.19
euro = real / 5.29
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(real, dolar, euro))



peca1, quantidade1, valor1 = str ( input ()).split()
peca2, quantidade2, valor2 = str ( input ()).split()

peca1 = int (peca1)
quantidade1 = int (quantidade1)
valor1 = round ( float ( valor1), 2)

peca2 = int( peca2)
quantidade2 = int( quantidade2)
valor2 = round ( float (valor2), 2)

total1 = quantidade1*valor1
total2 = quantidade2*valor2

total = total1 + total2

print (f'VALOR A PAGAR: R$ {total:.2f}')
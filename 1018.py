#variaveis 
notas001 = int(input())

print (notas001)

#100
notas100 = notas001//100
notas001 = notas001%100

#50

notas050 = notas001//50
notas001 = notas001%50

#20
notas020 = notas001//20
notas001 = notas001%20

#10
notas010 = notas001//10
notas001 = notas001%10

#5
notas005 = notas001//5
notas001 = notas001%5

#2
notas002 = notas001//2
notas001 = notas001%2

print(f'{notas100:.0f} notas(s) de R$ 100,00')
print(f'{notas050:.0f} notas(s) de R$ 50,00')
print(f'{notas020:.0f} notas(s) de R$ 20,00')
print(f'{notas010:.0f} notas(s) de R$ 10,00')
print(f'{notas005:.0f} notas(s) de R$ 5,00')
print(f'{notas002:.0f} notas(s) de R$ 2,00')
print(f'{notas001:.0f} notas(s) de R$ 1,00')
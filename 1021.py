#variaveis 

valor = float(input())

nota100 = valor//100
nota050 = valor % 100 // 50
nota020 = valor % 100 % 50 // 20 
nota010 = valor % 100 % 50 % 20 // 10
nota5 = valor % 100 % 50 % 20 % 10 // 5 
nota2 = valor % 100 % 50 % 20 % 10 % 5 // 2 
moeda1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1 
moeda50 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 // 0.50
moeda25 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 // 0.25
moeda10 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 // 0.10
moeda5 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 //0.05
moeda01 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01 + 0.01

print ('NOTAS:')
print (f'{nota100:.0f} nota(s) de R$ 100.00')
print (f'{nota050:.0f} nota(s) de R$ 50.00')
print (f'{nota020:.0f} nota(s) de R$ 20.00')
print (f'{nota010:.0f} nota(s) de R$ 10.00')
print (f'{nota5:.0f} nota(s) de R$ 5.00')
print (f'{nota2:.0f} nota(s) de R$ 2.00')
print ('MOEDAS:')
print (f'{moeda1:.0f} nota(s) de R$ 1.00')
print (f'{moeda50:.0f} nota(s) de R$ 0.50')
print (f'{moeda25:.0f} nota(s) de R$ 0.25')
print (f'{moeda10:.0f} nota(s) de R$ 0.10')
print (f'{moeda5:.0f} nota(s) de R$ 0.05')
print (f'{moeda01:.0f} nota(s) de R$ 0.01')
nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas/100*15
porc = salario + comissao
print (F"TOTAL = R${porc:.2f}")
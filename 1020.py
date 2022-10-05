#variaveis 
dias = int(input())

ano = dias//365
dias = dias%365

meses = dias//30
dias = dias%30 

dia = dias//1
dias = dias%1

print (f'{ano} ano(s)')
print (f'{meses} mes(es)')
print (f'{dia} dia(s)')
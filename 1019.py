#variaveis 
segundos = int(input())

horas = segundos//3600
segundos = segundos%3600

minutos = segundos//60
segundos = segundos%60

segundos1 = segundos//1
segundos = segundos%1

print (f"{horas}:{minutos}:{segundos1}")
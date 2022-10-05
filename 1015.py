#Variaveis a serem inseridas 
x1, y1, x2, y2 = str (input()).split()

x_1 = float (x1)
y_1 = float (y1)
x_2 = float (x2)
y_2 = float (y2)

distancia = ((x_2 - x_1)**2+(y_2-y_1)**2)**(1/2)

print (f"{distancia:.4f}")
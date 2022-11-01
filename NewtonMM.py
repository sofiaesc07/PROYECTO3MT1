 #Ana Sofia Escobar Rivera
#Carnet 20489

#librerias a importar
import numpy as np


#Plantear la funcion con sus derivadas
def Y(X):
    return -X**3 + 6*X**2 + 15*X -15
def d1Y(X):
    return -3*X**2 +12*X + 15
def d2Y(X):
    return  -6*X+12

#Plantear una funcion para el metodo
def NewtonRaphson():
    #valores de x
    a, b = 4,7
    #valor cercano
    x = 3
    epsilon = 0.01
    
    cont = 0
    registro = []
    
    while True:
        # Calculo de f'(x) y f''(x)
        d1Y_x = d1Y(x)
        d2Y_x = d2Y(x)
        xprev = x
        x = xprev - d1Y_x/d2Y_x
        
        Y_x = Y(x)
        #pasos para crear y mostrar las iteraciones
        cont = cont + 1
        registro.append([cont, x, Y_x])
        
        print("Iteraciones: {:2d} - X: {:.10f} - Y: {:.10f} - Error: {:.10}".format(cont, x, Y_x,np.abs(x - xprev)))
        #error
        if(np.abs(x - xprev) <= epsilon):
            print("")
            print("Iteraciones totales: {:2d} - X final: {:.10f} - Y final: {:.10f} - Error final: {:.10}".format(cont, x, Y_x,np.abs(x - xprev)))
            break     
    return registro

NewtonRaphson()
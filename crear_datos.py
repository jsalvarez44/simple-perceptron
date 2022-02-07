import random as rd

def crear_datos_prueba():
    matriz = [[None] * 3 for i in range(1000)]   
    
    for i in range(1000):
        for j in range(3):
            if (j == 0):
                matriz[i][j] = 1.0
            else:
                matriz[i][j] = rd.uniform(0, 2)

    f = open('datos_prueba.txt','w')
    
    for i in range(len(matriz)):
        f.write(str(matriz[i]))
        f.write(',\n')
        
    f.close()

def crear_datos_entrenamiento():
    matriz = [[None] * 4 for i in range(100)]   
    
    for i in range(100):
        for j in range(4):
            if (j == 0):
                matriz[i][j] = 1.0
            elif (j>0 and j<3):
                matriz[i][j] = rd.uniform(0, 2)
            else:
                if(matriz[i][2] >= 1): matriz[i][j] = 1.0
                else: matriz[i][j] = 0.0

    f = open('datos_entrenamiento.txt','w')
    
    for i in range(len(matriz)):
        f.write(str(matriz[i]))
        f.write(',\n')
        
    f.close()
    

#crear_datos_prueba()
crear_datos_entrenamiento()

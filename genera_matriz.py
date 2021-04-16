import numpy as np

<<<<<<< HEAD
def crear_matriz(probabilidades): ##Genera una matriz de numeros enteros aleatorios 
    matriz = np.random.choice(5,(15,15),p=probabilidades)
    return matriz

def guardar_matriz(fname, num_array): ##guarda la matriz :V
    a = open(fname, "w")
    np.savetxt(a,matriz,fmt='%d',delimiter=',')

    a.close()
    
def obtener_probabilidades(numero_probabilidades):
    total = 1.0
    probabilidad_restante = total
    probabilidades = []
    for i in range(numero_probabilidades):
        if(i < numero_probabilidades-1):
            probabilidad = probabilidad_restante  * np.random.random_sample() 
            probabilidad_restante = probabilidad_restante - probabilidad
            probabilidades.append(probabilidad)
            '''print("probabilidad:",probabilidad)
            print("probabilidad restante",probabilidad_restante)'''
        else:
            probabilidades.append(probabilidad_restante)
            probabilidad_restante = 0
            '''print("probabilidad:",probabilidad)
            print("probabilidad restante",probabilidad_restante)'''
        print(probabilidades)

if __name__ == '__main__':
    probabilidades= obtener_probabilidades(5)
    fname = "matriz_aleatoria.txt"
    matriz = crear_matriz(probabilidades)
    guardar_matriz(fname,matriz)
    print(np.loadtxt(fname,dtype=int,delimiter=','))
=======
def crear_matriz(probabilidades, forma): #Crea una matriz de numeros aleatorios
    matriz = np.random.choice(5,forma,probabilidades)
    return matriz

def guardar_matriz(fname,matriz): #guarda una matriz :V
    a = open(fname, "w")
    np.savetxt(a, matriz, fmt='%d', delimiter=',')
    a.close()
    
def cargar_matriz(fname): #carga una matriz :VVVVV
    matriz = np.loadtxt(fname, dtype=int,delimiter =  ',')
    return matriz
    
def generar_probabilidades(n_probabilidades): ##genera las probabilidades de 
    probabilidades = []                       ##parecer de cada numero de  
    probabilidad_restante = 1                 ##la matriz
    for i in range(n_probabilidades):
        if (i < n_probabilidades-1):
            probabilidad = probabilidad_restante * np.random.sample()
            probabilidad_restante -= probabilidad
            probabilidades.append(probabilidad)
    probabilidad = probabilidad_restante 
    probabilidad_restante = 0
    probabilidades.append(probabilidad)
    return probabilidades

if __name__ == '__main__':
    probabilidades = generar_probabilidades(5) 
    fname = "matriz_aleatoria.txt"
    forma = (15,15)
    matriz = crear_matriz(probabilidades,forma)
    guardar_matriz(fname,matriz)
    print(cargar_matriz(fname))

>>>>>>> 846462c8902aaab9294aa24b1da31275f0f482dd

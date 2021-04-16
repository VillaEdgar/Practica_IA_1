import numpy as np

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

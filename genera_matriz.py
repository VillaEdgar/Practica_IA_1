import numpy as np

def crear_matriz():
    matriz = np.random.randint(0,9,(10,10),'int')
    return matriz

def guardar_matriz(fname, num_array):
    a = open("test.txt", "w")
    for fila in matriz:
        np.savetxt(a, fila)
    
    a.close()

if __name__ == '__main__':
    matriz = crear_matriz()
    guardar_matriz("prueba.txt",matriz)


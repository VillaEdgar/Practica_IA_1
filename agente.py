import genera_matriz as ma

matriz = ma.cargar_matriz('matriz_aleatoria.txt')
fil = matriz.shape[0]
col = matriz.shape[1]

params = {}             #Se crea el diccionario de parametros

for x in range(0, fil):
    for y in range(0, col):
        params[(x, y)] = (('V', False), ('O', False),   ##Se crea una lista de tuplas que definen los
                          ('I', False), ('X', False))   ##parámetros de cada casilla y se asignan al
        print(params[(x,y)])                                                ##diccionario según sus coordenadas


humano={0:False,1:1,2:2,3:3,4:4,5:5,6:5}

print(matriz[0][0])

def agente():


    return param
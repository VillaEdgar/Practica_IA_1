import genera_matriz as ma

matriz = ma.cargar_matriz('matriz_aleatoria.txt')
col= matriz.shape[0]
fil = matriz.shape[1]


paramsd = {}  # Se crea el diccionario de parametros

for x in range(0, fil):
    for y in range(0, col):
        params[(x, y)] = (('V', False), ('O', False), ('I', False), ('X', False), ('S',False))

params[(0, 5)] = (('V', False), ('O', False), ('I', True), ('X', False), ('S',False))


humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5}

def agente():

    for i in range(0, fil):
        for j in range(0, col):
            lista_params = params[(i, j)]
            for param in lista_params:
                if(param[0]=='I'):
                   if(param[1]):
                    print(param)
                    print(i,j)
agente()

for x in range(0, fil):
    for y in range(0, col):
        paramsd[(x, y)] = {'V': False, 'O': False, 'I': False, 'X': False, 'S':False}

paramsd[(5, 0)] = {'V': False, 'O': False, 'I': True, 'X': False, 'S':False}

humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5} #definicion humano

'''for x in range(0, fil):
    print()
    for y in range(0, col):

        print(str(x),str(y), paramsd[(x, y)])
'''

def spawn(paramsd):
    for i in range(0, fil):
        for j in range(0, col):
            if(paramsd[(i,j)]['I']):

                paramsd[(i,j)]['V']=True
                paramsd[(i,j)]['S'] = True
                paramsd[(i,j)]['X'] = True
                #
    #return paramsd

spawn(paramsd)

def sense(paramsd):

    for i in range(0, fil):
        for j in range(0, col):

            if (paramsd[(i, j)]['X']):

                paramsd[(i, j)]['S'] = True

                if(i>0):
                    paramsd[(i-1, j)]['S']= True
                if(i<fil-1):
                    paramsd[(i+1,j)]['S'] = True
                if ( j>0):
                    paramsd[(i, j-1)]['S']= True
                    print(j-1)

                if (j < col-1):
                    paramsd[(i, j+1)]['S']= True



   #return paramsd


sense(paramsd)

def step(paramsd):

    for i in range(0, fil):
        for j in range(0, col):
                if paramsd[(i, j)]['X']:

                    paramsd[(i, j)]['V'] = True

                    if (i-1 > 0):
                        if(humano[matriz[i-1][j]]):
                            paramsd[(i, j)]['X']=False
                            paramsd[(i-1, j)]['X']=True
                            return paramsd

                    if (j - 1 > 0):
                        if (humano[matriz[i - 1][j]]):
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j - 1)]['X'] = True

                            return paramsd

                    if(i+1 < fil-1 ):
                        if (humano[matriz[i - 1][j]]):
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i +1, j)]['X'] = True

                            return paramsd

                    if (j+1 < col-1):
                        if (humano[matriz[i - 1][j]]):
                            paramsd[(i, j)]['X'] = False
                            paramsd[(i, j+1)]['X'] = True
                            return paramsd





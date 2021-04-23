humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5} #definicion humano

'''for x in range(0, fil):
    print()
    for y in range(0, col):

        print(str(x),str(y), paramsd[(x, y)])
'''

def spawn(paramsd,matriz):
    col= matriz.shape[0]
    fil = matriz.shape[1]
    for i in range(0, fil):
        for j in range(0, col):
            if(paramsd[(i,j)]['I']):

                paramsd[(i,j)]['V']=True
                paramsd[(i,j)]['S'] = True
                paramsd[(i,j)]['X'] = True
                #
    return paramsd


def sense(paramsd, matriz):
    col= matriz.shape[0]
    fil = matriz.shape[1]

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
    return paramsd

def step(paramsd, matriz):

    col= matriz.shape[0]
    fil = matriz.shape[1]
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





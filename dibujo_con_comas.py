import pygame
BLACK = (0, 0, 0)

blueP = (20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
pinkP= (255,77,195)
greyP = (160, 160, 160)
aquaP = (90,139,185)
yellowP = (255,255,0)
purpleP = (102,0,102)
whiteP = (255,255,255)
brownP = (102,51,0)

sizeSquare = 40
sizeCuadricula = 10
count=0
#px = int(eval(input("Coordenada en X: ")))
#py = int(eval(input("Coordenada en Y: ")))
px = 1
py = 1

x = 0
y = 0
pygame.init()
tamaño_ventana = (sizeSquare*sizeCuadricula, sizeSquare*sizeCuadricula)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False


while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    fichero=open('matriz_aleatoria.txt','r')
    ventana.fill(BLACK)
    Fuente = pygame.font.SysFont('fontname', 16)
    Tx = 0
    Ty = 0
    for i in range(1, tamaño_ventana[0], 40):
    	linea = fichero.readline()
    	if linea != '':
    		count=0
	    	for j in range(1, tamaño_ventana[1], 40):
	    		#print(count)
	    		while linea[count]==',':
	    			count=count+1
	    		if linea[count] == '0':
	    			pygame.draw.rect(ventana, greyP, [j, i, 38, 38], 0)
	    		elif linea[count] == '1':
	    			pygame.draw.rect(ventana, brownP, [j, i, 38, 38], 0)
	    		elif linea[count] == '2':
	    			pygame.draw.rect(ventana, blueP, [j, i, 38, 38], 0)
	    		elif linea[count] == '3':
	    			pygame.draw.rect(ventana, yellowP, [j, i, 38, 38], 0)
	    		elif linea[count] == '4':
	    			pygame.draw.rect(ventana, greenP, [j, i, 38, 38], 0)
	    		elif linea[count] == '5':
	    			pygame.draw.rect(ventana, aquaP, [j, i, 38, 38], 0)
	    		elif linea[count] == '6':
	    			pygame.draw.rect(ventana, pinkP, [j, i, 38, 38], 0)
	    		elif linea[count] == '7':
	    			pygame.draw.rect(ventana, purpleP, [j, i, 38, 38], 0)
	    		elif linea[count] == '8':
	    			pygame.draw.rect(ventana, whiteP, [j, i, 38, 38], 0)
	    		elif linea[count] == '9':
	    			pygame.draw.rect(ventana, redP, [j, i, 38, 38], 0)
	    		count=count+1
    	count=0
    	Texto = Fuente.render(str(Tx), True, BLACK)
    	ventana.blit(Texto, [i, 2])
    	if Tx != 0:
    		ventana.blit(Texto, [2, i + 16])
    	Tx += 1
    	Ty = 0
    fichero.close()
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
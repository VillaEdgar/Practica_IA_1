import pygame
import random
BLACK = (0, 0, 0)

water = (0, 0, 255)
forest = (6, 71, 12)
redP = (230, 0, 20)
pinkP= (255,77,195)
mountains = (160, 160, 160)
aquaP = (90,139,185)
sand = (194, 178, 128)
purpleP = (102,0,102)
whiteP = (255,255,255)
land = (181, 101, 29)

colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

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
size = (sizeSquare*sizeCuadricula, sizeSquare*sizeCuadricula)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    fichero=open('matriz_aleatoria.txt','r')
    screen.fill(BLACK)
    Fuente = pygame.font.SysFont('fontname', 16)
    Tx = 0
    Ty = 0
    for i in range(1, size[0], 40):
    	linea = fichero.readline()
    	if linea != '':
    		count=0
	    	for j in range(1, size[1], 40):
	    		#print(count)
	    		while linea[count]==',':
	    			count=count+1
	    		if linea[count] == '0':
	    			pygame.draw.rect(screen, mountains, [j, i, 38, 38], 0)
	    		elif linea[count] == '1':
	    			pygame.draw.rect(screen, land, [j, i, 38, 38], 0)
	    		elif linea[count] == '2':
	    			pygame.draw.rect(screen, water, [j, i, 38, 38], 0)
	    		elif linea[count] == '3':
	    			pygame.draw.rect(screen, sand, [j, i, 38, 38], 0)
	    		elif linea[count] == '4':
	    			pygame.draw.rect(screen, forest, [j, i, 38, 38], 0)
	    		elif linea[count] == '5':
	    			pygame.draw.rect(screen, aquaP, [j, i, 38, 38], 0)
	    		elif linea[count] == '6':
	    			pygame.draw.rect(screen, redP, [j, i, 38, 38], 0)
	    		elif linea[count] == '7':
	    			pygame.draw.rect(screen, purpleP, [j, i, 38, 38], 0)
	    		elif linea[count] == '8':
	    			pygame.draw.rect(screen, whiteP, [j, i, 38, 38], 0)
	    		elif linea[count] == '9':
	    			pygame.draw.rect(screen, pinkP, [j, i, 38, 38], 0)
	    		count=count+1
    	count=0
    	Texto = Fuente.render(str(Tx), True, BLACK)
    	screen.blit(Texto, [i, 2])
    	if Tx != 0:
    		screen.blit(Texto, [2, i + 16])
    	Tx += 1
    	Ty = 0
    fichero.close()
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
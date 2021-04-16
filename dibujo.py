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

#tamañoCasilla es el tamaño que tendrá cada lado de las casillas
tamañoCasilla = 40

#tamañoCuadricula es el numero de casillas que tendrá la cuadricula por lado 
tamañoCuadricula = 15
contador=0

pygame.init()

#tamañoPantalla es el una tupla con los valores del tamaño de la pantalla
tamañoPantalla = (tamañoCasilla*tamañoCuadricula, tamañoCasilla*tamañoCuadricula)

#pantall es la pantalla a desplegar
pantalla = pygame.display.set_mode(tamañoPantalla)

#se le da un titulo a la ventana a desplegar
pygame.display.set_caption("Grid on PYGAME")

#reloj es un timer que indica la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

#gameOver el el indicador de querer cerrar la pantalla
gameOver = False

#Fuente es un estilo de imagen inicializada dentro de pygame. Pygame solo muestra imagenes o dibujos, no texto.
Fuente = pygame.font.SysFont('fontname', 16)
#VOIX son letras combertidas en imagenes para mostrarlas en pantalla.
V = Fuente.render('V', True, BLACK)
O = Fuente.render('O', True, BLACK)
I = Fuente.render('I', True, BLACK)
X = Fuente.render('X', True, BLACK)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    fichero=open('matriz_aleatoria.txt','r')
    pantalla.fill(BLACK) #La pantalla se llena de un fondo negro.

    #T es un contador para pintar las coordenadas
    T = 0
    for i in range(1, tamañoPantalla[0], 40):#este for recorre el ancho de la pantalla
    	linea = fichero.readline()
    	if linea != '':
    		contador=0
	    	for j in range(1, tamañoPantalla[1], 40):#este for recorre el alto de la pantalla
	    		#print(contador)
	    		while linea[contador]==',':
	    			contador=contador+1
	    		if linea[contador] == '0':
	    			pygame.draw.rect(pantalla, mountains, [j, i, 38, 38], 0)#Los cuadros son ligeramente más pequeños para dar el efecto de la cuadricula.
	    		elif linea[contador] == '1':
	    			pygame.draw.rect(pantalla, land, [j, i, 38, 38], 0)
	    		elif linea[contador] == '2':
	    			pygame.draw.rect(pantalla, water, [j, i, 38, 38], 0)
	    		elif linea[contador] == '3':
	    			pygame.draw.rect(pantalla, sand, [j, i, 38, 38], 0)
	    		elif linea[contador] == '4':
	    			pygame.draw.rect(pantalla, forest, [j, i, 38, 38], 0)
	    		elif linea[contador] == '5':
	    			pygame.draw.rect(pantalla, aquaP, [j, i, 38, 38], 0)
	    		elif linea[contador] == '6':
	    			pygame.draw.rect(pantalla, redP, [j, i, 38, 38], 0)
	    		elif linea[contador] == '7':
	    			pygame.draw.rect(pantalla, purpleP, [j, i, 38, 38], 0)
	    		elif linea[contador] == '8':
	    			pygame.draw.rect(pantalla, whiteP, [j, i, 38, 38], 0)
	    		elif linea[contador] == '9':
	    			pygame.draw.rect(pantalla, pinkP, [j, i, 38, 38], 0)
	    		contador=contador+1

	    		pantalla.blit(V,[j+3,i+26])
	    		pantalla.blit(O,[j+12,i+26])
	    		pantalla.blit(I,[j+24,i+26])
	    		pantalla.blit(X,[j+30,i+26])
    	
    	#Texto es la imagen con la que se pintarán las coordenadas
    	Texto = Fuente.render(str(T), True, BLACK)
    	pantalla.blit(Texto, [i, 2])#Coordenadas en el eje X
    	if T != 0:
    		pantalla.blit(Texto, [2, i])#Coordenadas en el eje Y
    	T += 1
    fichero.close()
    pygame.display.flip()
    reloj.tick(5)
pygame.quit()
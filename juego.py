import pygame, sys
from pygame.locals import *
from random import randint
"""
def moneda(x,y):
	moneda=pygame.sprite.Sprite()
	moneda.image =coin
	moneda.rect = coin.get_rect()
	moneda.rect.top = y
	moneda.rect.left = x
	PANTALLA.blit(moneda.image,moneda.rect)

def personaje(x,y):
	pingu=pygame.sprite.Sprite()
	pingu.image = pinguino
	pingu.rect = pinguino.get_rect()
	pingu.rect.top = y
	pingu.rect.left = x
	PANTALLA.blit(pingu.image,pingu.rect)

def disparo(x,y):
	proyectil=pygame.sprite.Sprite()
	proyectil.image =bala
	proyectil.rect = bala.get_rect()
	proyectil.rect.top = y + 5
	proyectil.rect.left = x + 5+
	PANTALLA.blit(proyectil.image,proyectil.rect)
"""
pygame.init()

PANTALLA = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Tecbianito')
aumX = 0
aumY = 0
aumX2 = 0
aumY2 = 0
PERSONAJEX=10
PERSONAJEY=530
PERSONAJEX2=740
PERSONAJEY2=530
"""Cargando Imagenes"""
coin = pygame.image.load("coinmin.png")
pinguino = pygame.image.load("jugadormin1.png")
pinguino2 = pygame.image.load("clipmin.png")
bala = pygame.image.load("newbala.png")

reloj = pygame.time.Clock()

"""Variables iniciales"""
coinx=randint(10,790)
coiny=randint(10,590)

puntos=0
puntos2=0
fuente=pygame.font.Font(None,25)

"""Creo los sprites"""
pingu=pygame.sprite.Sprite()
pingu.image = pinguino
pingu.rect = pinguino.get_rect()
pingu.rect.top = PERSONAJEY
pingu.rect.left = PERSONAJEX


pingu2=pygame.sprite.Sprite()
pingu2.image = pinguino2
pingu2.rect = pinguino2.get_rect()
pingu2.rect.top = PERSONAJEY2
pingu2.rect.left = PERSONAJEX2

moneda=pygame.sprite.Sprite()
moneda.image =coin
moneda.rect = coin.get_rect()

proyectil=pygame.sprite.Sprite()
proyectil.image =bala
proyectil.rect = bala.get_rect()

proyectil2=pygame.sprite.Sprite()
proyectil2.image =bala
proyectil2.rect = bala.get_rect()

"""Variables iniciales"""
disparo=False
disparo2=False
vivo=True
tiempo=0
vivo2=True
tiempo2=0

while True:
	PANTALLA.fill((0,0,0))
	"""Jugador 1 vivo-muerto"""
	if pingu.rect.colliderect(proyectil2.rect):
		vivo2=False
	if vivo2:
		pingu.rect.top = PERSONAJEY
		pingu.rect.left = PERSONAJEX
		PANTALLA.blit(pingu.image,pingu.rect)
	else:
		tiempo2+=1

	if tiempo2==120:
		PERSONAJEX=10
		PERSONAJEY=530
		tiempo2=0
		vivo2=True
	

	"""Jugador 2 vivo-muerto"""
	if pingu2.rect.colliderect(proyectil.rect):
		vivo=False

	if vivo:
		pingu2.rect.top = PERSONAJEY2
		pingu2.rect.left = PERSONAJEX2
		PANTALLA.blit(pingu2.image,pingu2.rect)
	else:
		tiempo+=1

	if tiempo==120:
		PERSONAJEX2=740
		PERSONAJEY2=530
		tiempo=0
		vivo=True
		

	"""moneda aparicion aleatoria"""
	moneda.rect.top = coiny
	moneda.rect.left = coinx
	PANTALLA.blit(moneda.image,moneda.rect)
	
	"""contar los puntos Jug1"""
	puntosimp=fuente.render("Player1 Puntos: "+str(puntos),0,(200,60,80))
	PANTALLA.blit(puntosimp,(10,10))

	"""contar los puntos Jug1"""
	puntosimp2=fuente.render("Player2 Puntos: "+str(puntos2),0,(200,60,80))
	PANTALLA.blit(puntosimp2,(620,10))


	"""Disparo Jug1"""
	if disparo:
		PANTALLA.blit(proyectil.image,proyectil.rect) 
	"""Disparo Jug2"""
	if disparo2:
		PANTALLA.blit(proyectil2.image,proyectil2.rect)
	"""Colision con moneda , suma punto Jug1"""
	if pingu.rect.colliderect(moneda.rect):
		coinx=randint(10,790)
		coiny=randint(10,590)
		puntos+=1
	"""Colision con moneda , suma punto Jug2"""
	if pingu2.rect.colliderect(moneda.rect):
		coinx=randint(10,790)
		coiny=randint(10,590)
		puntos2+=1


	"""Acciones teclas"""
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				aumX = 5
			if event.key == pygame.K_a:
				aumX = -5
			if event.key == pygame.K_w:
				aumY = -5
			if event.key == pygame.K_s:
				aumY = +5
			if event.key == pygame.K_RIGHT:
				aumX2 = 5
			if event.key == pygame.K_LEFT:
				aumX2 = -5
			if event.key == pygame.K_UP:
				aumY2 = -5
			if event.key == pygame.K_DOWN:
				aumY2 = +5
			if event.key == pygame.K_SPACE:
				disparo=True
				proyectil.rect.left = PERSONAJEX +30
				proyectil.rect.top =  PERSONAJEY +33
			if event.key == pygame.K_KP5:
				disparo2=True
				proyectil2.rect.left = PERSONAJEX2 +30
				proyectil2.rect.top =  PERSONAJEY2 +33
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				aumX = 0
			if event.key == pygame.K_a:
				aumX = 0
			if event.key == pygame.K_w:
				aumY = 0
			if event.key == pygame.K_s:
				aumY = 0
			if event.key == pygame.K_RIGHT:
				aumX2 = 0
			if event.key == pygame.K_LEFT:
				aumX2 = 0
			if event.key == pygame.K_UP:
				aumY2 = 0
			if event.key == pygame.K_DOWN:
				aumY2 = 0
	"""Recorrido de bala Jug1"""
	if disparo:
		proyectil.rect.left += 20
		if proyectil.rect.left > 1200:
			disparo = False
	"""Recorrido de bala Jug2"""
	if disparo2:
		proyectil2.rect.left -= 20
		if proyectil2.rect.left <-1200:
			disparo2 = False
	"""Variables que uso para aumentar el valor de la posicion cuando apretamos una tecla Jug1"""
	PERSONAJEX=PERSONAJEX+aumX
	PERSONAJEY=PERSONAJEY+aumY
	"""Variables que uso para aumentar el valor de la posicion cuando apretamos una tecla Jug2"""
	PERSONAJEX2=PERSONAJEX2+aumX2
	PERSONAJEY2=PERSONAJEY2+aumY2

	reloj.tick(100)
	pygame.display.flip()
	pygame.display.update()

import pygame
import random
import threading, time
import asyncio

async def main():

    MORADO = (128, 0, 128)
    BLANCO = (255,255,255)	
    AMARILLO = (255,255,0)
    AZUL_FANTASMA = (173,216,230)
    ROSA_FANTASMA = (255,203,219)
    NARANJA_FANTASMA = (255,146,32)
    ROJO_FANTASMA = (254,0,0)

    LARGO_PANTALLA = 655
    ANCHO_PANTALLA = 675  

    def crearProtagonista(spritesProtagonista):
        
        protagonista = pygame.sprite.Sprite()
        imagenPacman = pygame.image.load("sprites\Pacman_LadoDerecho-removebg-preview-removebg-preview (2).png")
        protagonista.image = imagenPacman
        
        
        protagonista.rect = protagonista.image.get_rect()
        protagonista.rect.x = 325
        protagonista.rect.y = 609
        
        protagonista.velocidad_x = 0
        protagonista.velocidad_y = 0
        
        spritesProtagonista.add(protagonista)
        
        return protagonista

    def cambioVelocidadProtagonista(protagonista, x, y):
        protagonista.velocidad_x += x
        protagonista.velocidad_y += y

    def updateProtagonista(protagonista, paredes):
        
        protagonista.rect.x += protagonista.velocidad_x

        lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, paredes, False)
        for bloque in lista_impactos_bloques:
            if protagonista.velocidad_x <= 0:
                protagonista.rect.left = bloque.rect.right
            else:
                protagonista.rect.right = bloque.rect.left
        protagonista.rect.y += protagonista.velocidad_y
        
        lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, paredes, False)
        for bloque in lista_impactos_bloques:
            if protagonista.velocidad_y <= 0:
                protagonista.rect.top = bloque.rect.bottom
            else:
                protagonista.rect.bottom = bloque.rect.top

    def aparecerLadoContrario(protagonista):
        
        if (protagonista.rect.right < 0):
            protagonista.rect.left = ANCHO_PANTALLA
        elif(protagonista.rect.left > ANCHO_PANTALLA):
            protagonista.rect.right = 0

        return protagonista

    def crearFantasmaAzul(spritesFantasma):

        fantasmaAzul = pygame.sprite.Sprite()
        imagenFantasmaAzul = pygame.image.load("sprites\FantasmaAzul-removebg-preview (2) (1).png")
        fantasmaAzul.image = imagenFantasmaAzul 

        fantasmaAzul.rect = fantasmaAzul.image.get_rect()
        fantasmaAzul.rect.x = 262
        fantasmaAzul.rect.y = 292

        fantasmaAzul.velocidad_x = random.randint(1,2)
        fantasmaAzul.velocidad_y = random.randint(1,2)

        spritesFantasma.add(fantasmaAzul)

        return fantasmaAzul

    def crearFantasmaRosa(spritesFantasma):

        fantasmaRosa = pygame.sprite.Sprite()
        imagenFantasmaRosa = pygame.image.load("sprites\FantasmaRosa-removebg-preview (3) (1).png")
        fantasmaRosa.image = imagenFantasmaRosa

        fantasmaRosa.rect = fantasmaRosa.image.get_rect()
        fantasmaRosa.rect.x = 295
        fantasmaRosa.rect.y = 292

        fantasmaRosa.velocidad_x = random.randint(1,2)
        fantasmaRosa.velocidad_y = random.randint(1,2)

        spritesFantasma.add(fantasmaRosa)

        return fantasmaRosa

    def crearFantasmaRojo(spritesFantasma):

        fantasmaRojo = pygame.sprite.Sprite()
        imagenFantasmaRojo = pygame.image.load("sprites\FantasmaRojo-removebg-preview (2) (1).png")
        fantasmaRojo.image = imagenFantasmaRojo 

        fantasmaRojo.rect = fantasmaRojo.image.get_rect()
        fantasmaRojo.rect.x = 355
        fantasmaRojo.rect.y = 292

        fantasmaRojo.velocidad_x = random.randint(1,2)
        fantasmaRojo.velocidad_y = random.randint(1,2)

        spritesFantasma.add(fantasmaRojo)

        return fantasmaRojo

    def crearFantasmaNaranja(spritesFantasma):

        fantasmaNaranja = pygame.sprite.Sprite()
        imagenFantasmaNaranja = pygame.image.load("sprites\FantasmaNaranja-removebg-preview (2) (1).png")
        fantasmaNaranja.image = imagenFantasmaNaranja

        fantasmaNaranja.rect = fantasmaNaranja.image.get_rect()
        fantasmaNaranja.rect.x = 382
        fantasmaNaranja.rect.y = 292

        fantasmaNaranja.velocidad_x = random.randint(1,2)
        fantasmaNaranja.velocidad_y = random.randint(1,2)

        spritesFantasma.add(fantasmaNaranja)

        return fantasmaNaranja

    def updateFantasmas(fantasma, paredes):
        
        fantasma.rect.x += fantasma.velocidad_x

        lista_impactos_bloques = pygame.sprite.spritecollide(fantasma, paredes, False)
        for bloque in lista_impactos_bloques:
            if fantasma.velocidad_x <= 0:
                fantasma.rect.left = bloque.rect.right
                movimientoFantasma(4, fantasma)
            else:
                fantasma.rect.right = bloque.rect.left
                movimientoFantasma(3, fantasma)

        fantasma.rect.y += fantasma.velocidad_y

        lista_impactos_bloques = pygame.sprite.spritecollide(fantasma, paredes, False)
        for bloque in lista_impactos_bloques:
            if fantasma.velocidad_y <= 0:
                fantasma.rect.top = bloque.rect.bottom
                movimientoFantasma(2, fantasma)
            else:
                fantasma.rect.bottom = bloque.rect.top
                movimientoFantasma(1, fantasma)

    def movimientoFantasma(num, fantasma):

        num = random.randint(1,4)
        
        if num == 1:
            fantasma.velocidad_x = 2
            fantasma.velocidad_y = 0
        elif num == 2:
            fantasma.velocidad_x = 0
            fantasma.velocidad_y = 2
        elif num == 3:
            fantasma.velocidad_x = -2
            fantasma.velocidad_y = 0
        elif num == 4:
            fantasma.velocidad_x = 0
            fantasma.velocidad_y = -2

    def salirJaulaFantasma(fantasma):

        if((fantasma.rect.x >= 311) and (fantasma.rect.x <= 333)) and ((fantasma.rect.y >= 270) and (fantasma.rect.y <= 333)):
            fantasma.velocidad_x = 0
            fantasma.velocidad_y = -1

    def aparecerLadoContrarioFantasma(fantasma):
        
        if (fantasma.rect.right < 0):
            fantasma.rect.left = ANCHO_PANTALLA
        elif(fantasma.rect.left > ANCHO_PANTALLA):
            fantasma.rect.right = 0
        return fantasma

    def colisionFantasmasPacmanVidaMenos(protagonista, fantasma):

        lista_impactos_fantasmasPacman = pygame.sprite.collide_rect(protagonista, fantasma)
        
        if lista_impactos_fantasmasPacman:
            protagonista.rect.x = 325
            protagonista.rect.y = 609
            protagonista.velocidad_x = 0
            protagonista.velocidad_y = 0
        return lista_impactos_fantasmasPacman

    def pacmanComeFantasmas(protagonista, fantasma, x, y):

        lista_impactos_fantasmasPacman = pygame.sprite.collide_rect(protagonista, fantasma)
        
        if lista_impactos_fantasmasPacman:
            protagonista.rect.x = x
            protagonista.rect.y = y
        return lista_impactos_fantasmasPacman


    def crearBola(x, y, ancho, largo):
        
        bola = pygame.sprite.Sprite()
        
        bola.image = pygame.Surface([ancho, largo])
        bola.image.fill(BLANCO)
        
        bola.rect = bola.image.get_rect()
        bola.rect.y = y
        bola.rect.x = x
        
        return bola

    def createBolas(spritesDelJuego):

        listaBolas = pygame.sprite.Group()

        #Bolas arriba izquierda

        ball = crearBola(28,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(56,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(84,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(112,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(140,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(168,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(196,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas abajo izquierda

        ball = crearBola(28,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(56,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(84,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(112,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(140,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(168,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(196,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Derecha

        ball = crearBola(384,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(468,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(496,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(524,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(552,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(580,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(608,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(636,28,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas abajo derecha

        ball = crearBola(384,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(468,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(496,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(524,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(552,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(580,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(608,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(636,618,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Seguidas

        ball = crearBola(28,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(56,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(84,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(112,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(140,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(168,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(196,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(308,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(332,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(356,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(384,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(468,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(496,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(524,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(552,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(580,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(608,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(636,110,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Izquierda 1

        ball = crearBola(28,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(56,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(84,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(112,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(140,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Izquierda 2

        ball = crearBola(224,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Derecha 1

        ball = crearBola(384,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Derecha 2

        ball = crearBola(524,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(552,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(580,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(608,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(636,555,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Encima Jaula

        ball = crearBola(224,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(308,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(332,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(356,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(384,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,235,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Bajo Jaula

        ball = crearBola(224,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(308,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(332,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(356,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(384,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,365,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Izquierda Jaula

        ball = crearBola(224,263,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,291,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,309,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,337,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(200,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(172,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(144,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(116,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(88,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(60,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(32,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(4,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Derecha Jaula

        ball = crearBola(440,263,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,291,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,309,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,337,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(464,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(492,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(520,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(548,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(576,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(604,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(632,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(660,300,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Centro Izquierda

        ball = crearBola(28,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(56,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(84,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(112,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(140,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(168,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(196,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Centro Derecha

        ball = crearBola(384,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(468,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(496,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(524,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(552,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(580,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(608,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(636,425,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Abajo Centro Seguidas

        ball = crearBola(168,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(196,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(224,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(308,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(332,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(356,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(384,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(468,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(496,490,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Izquierda 1

        ball = crearBola(224,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(252,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(280,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Derecha 2

        ball = crearBola(384,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(412,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(440,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Izquierda 3

        ball = crearBola(65,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(93,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(121,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(149,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        #Bolas Arriba Derecha 4

        ball = crearBola(510,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(538,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(566,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        ball = crearBola(594,175,9,9)
        listaBolas.add(ball)
        spritesDelJuego.add(ball)

        return listaBolas

    def colisionBolas(protagonista, bolas, PUNTOS):
        c = False
        lista_impactos_bolas = pygame.sprite.spritecollide(protagonista, bolas, True)
        for comida in lista_impactos_bolas:
            PUNTOS+=25
            c = True
        return PUNTOS, c

    def puntuacion(pantalla, PUNTOS):
        letra = pygame.font.Font(None, 15).render("Puntuacion: " + str(PUNTOS), True, (255,255,255))
        pantalla.blit(letra,[17,220])

    def mostrarVidas(pantalla, VIDAS):
        letra = pygame.font.Font(None, 15).render("Vidas: " + str(VIDAS), True, (255,255,255))
        pantalla.blit(letra,[17,235])
    

    def crearFrutaEspecial(x, y):

        fruta = pygame.sprite.Sprite()
        imagenFruta = pygame.image.load("sprites\cerezas-removebg-preview (1).png")
        fruta.image = imagenFruta
        
        fruta.rect = fruta.image.get_rect()
        fruta.rect.y = y
        fruta.rect.x = x
        
        return fruta

    def createFrutaEspecial(spritesDelJuego):
        
        listaFutas = pygame.sprite.Group()

        fruit = crearFrutaEspecial(27, 174)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(628, 174)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(27, 492)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(628, 492)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(148, 69)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(506, 69)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(222, 394)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)

        fruit = crearFrutaEspecial(436, 394)
        listaFutas.add(fruit)
        spritesDelJuego.add(fruit)
        
        return listaFutas


    def colisionFrutas(protagonista, frutas):

        lista_impactos_frutas = pygame.sprite.spritecollide(protagonista, frutas, True)
        if lista_impactos_frutas:
            print("hola")   
        return lista_impactos_frutas

    '''THIS FUNCTION CREATES THE SPRITES OF THE WALLS'''
    def crearPared(x , y, ancho, largo):
        
        pared = pygame.sprite.Sprite()
        
        pared.image = pygame.Surface([ancho, largo])
        pared.image.fill(MORADO)
        pared.image.set_alpha(0)
        
        pared.rect = pared.image.get_rect()
        pared.rect.y = y
        pared.rect.x = x
        
        return pared

    '''THIS FUNCTION CREATES THE WALLS'''
    def createParedes(spritesDelJuego):
        
        listaParedes = pygame.sprite.Group()
        
        paredIzq_alta = crearPared(0,0,14,287)
        listaParedes.add(paredIzq_alta)
        spritesDelJuego.add(paredIzq_alta)

        bloqueIzq_alto = crearPared(10,200,122,87)
        listaParedes.add(bloqueIzq_alto)
        spritesDelJuego.add(bloqueIzq_alto)

        paredIzq_baja = crearPared(0,327,14,329)
        listaParedes.add(paredIzq_baja)
        spritesDelJuego.add(paredIzq_baja)

        bloqueIzq_bajo = crearPared(10,327,122,87)
        listaParedes.add(bloqueIzq_bajo)
        spritesDelJuego.add(bloqueIzq_bajo)
        
        paredArriba = crearPared(10,0,665,12)
        listaParedes.add(paredArriba)
        spritesDelJuego.add(paredArriba)
        
        paredAbajo = crearPared(10,643,655,12)
        listaParedes.add(paredAbajo)
        spritesDelJuego.add(paredAbajo)
        
        paredDer_alta = crearPared(660,0,15,287)
        listaParedes.add(paredDer_alta)
        spritesDelJuego.add(paredDer_alta)

        bloqueDer_alto = crearPared(538,200,127,87)
        listaParedes.add(bloqueDer_alto)
        spritesDelJuego.add(bloqueDer_alto)

        paredDer_baja = crearPared(660,327,15,329)
        listaParedes.add(paredDer_baja)
        spritesDelJuego.add(paredDer_baja)

        bloqueDer_bajo = crearPared(538,327,127,87)
        listaParedes.add(bloqueDer_bajo)
        spritesDelJuego.add(bloqueDer_bajo)

        bloqueCentro_arriba = crearPared(322,10,30,85)
        listaParedes.add(bloqueCentro_arriba)
        spritesDelJuego.add(bloqueCentro_arriba)

        bloqueArriba_IzqCorto = crearPared(59,54,73,40)
        listaParedes.add(bloqueArriba_IzqCorto)
        spritesDelJuego.add(bloqueArriba_IzqCorto)

        bloqueArriba_IzqLargo = crearPared(178,54,100,40)
        listaParedes.add(bloqueArriba_IzqLargo)
        spritesDelJuego.add(bloqueArriba_IzqLargo)

        bloqueArriba_DerLargo = crearPared(395,54,100,40)
        listaParedes.add(bloqueArriba_DerLargo)
        spritesDelJuego.add(bloqueArriba_DerLargo)

        bloqueArriba_DerCorto = crearPared(541,54,73,40)
        listaParedes.add(bloqueArriba_DerCorto)
        spritesDelJuego.add(bloqueArriba_DerCorto)

        bloqueArriba_IzqPequenio = crearPared(60,139,72,17)
        listaParedes.add(bloqueArriba_IzqPequenio)
        spritesDelJuego.add(bloqueArriba_IzqPequenio)

        bloqueArriba_DerPequenio = crearPared(541,139,73,17)
        listaParedes.add(bloqueArriba_DerPequenio)
        spritesDelJuego.add(bloqueArriba_DerPequenio)

        PaloTArribaHorizontal_Centro = crearPared(249,136,172,22)
        listaParedes.add(PaloTArribaHorizontal_Centro)
        spritesDelJuego.add(PaloTArribaHorizontal_Centro)

        PaloTArribaVertical_Centro = crearPared(322,158,30,60)
        listaParedes.add(PaloTArribaVertical_Centro)
        spritesDelJuego.add(PaloTArribaVertical_Centro)

        PaloTIzquierdaVertical_Izquierda = crearPared(178,139,27,146)
        listaParedes.add(PaloTIzquierdaVertical_Izquierda)
        spritesDelJuego.add(PaloTIzquierdaVertical_Izquierda)

        PaloTIzquierdaHorizontal_Izquierda = crearPared(204,200,70,22)
        listaParedes.add(PaloTIzquierdaHorizontal_Izquierda)
        spritesDelJuego.add(PaloTIzquierdaHorizontal_Izquierda)

        PaloTDerechaVertical_Derecha = crearPared(466,139,27,146)
        listaParedes.add(PaloTDerechaVertical_Derecha)
        spritesDelJuego.add(PaloTDerechaVertical_Derecha)

        PaloTDerechaHorizontal_Derecha = crearPared(395,200,72,22)
        listaParedes.add(PaloTDerechaHorizontal_Derecha)
        spritesDelJuego.add(PaloTDerechaHorizontal_Derecha)

        paredIzqJaula = crearPared(246,264,10,83)
        listaParedes.add(paredIzqJaula)
        spritesDelJuego.add(paredIzqJaula)

        paredDerJaula = crearPared(414,264,10,82)
        listaParedes.add(paredDerJaula)
        spritesDelJuego.add(paredDerJaula)

        paredArribaJaula_Izq = crearPared(246,262,65,11)
        listaParedes.add(paredArribaJaula_Izq)
        spritesDelJuego.add(paredArribaJaula_Izq)

        paredArribaJaula_Der = crearPared(358,262,66,11)
        listaParedes.add(paredArribaJaula_Der)
        spritesDelJuego.add(paredArribaJaula_Der)

        paredAbajoJaula = crearPared(246,335,178,13)
        listaParedes.add(paredAbajoJaula)
        spritesDelJuego.add(paredAbajoJaula)

        bloquePequenioVertical_Izq = crearPared(178,328,27,81)
        listaParedes.add(bloquePequenioVertical_Izq)
        spritesDelJuego.add(bloquePequenioVertical_Izq)

        bloquePequenioVertical_Der = crearPared(466,328,30,81)
        listaParedes.add(bloquePequenioVertical_Der)
        spritesDelJuego.add(bloquePequenioVertical_Der)

        PaloTAbajoHorizontal = crearPared(251,392,170,19)
        listaParedes.add(PaloTAbajoHorizontal)
        spritesDelJuego.add(PaloTAbajoHorizontal)

        PaloTAbajoVertical = crearPared(322,403,28,69)
        listaParedes.add(PaloTAbajoVertical)
        spritesDelJuego.add(PaloTAbajoVertical)

        PaloTAbajoHorizontal_gemela = crearPared(251,515,170,23)
        listaParedes.add(PaloTAbajoHorizontal_gemela)
        spritesDelJuego.add(PaloTAbajoHorizontal_gemela)

        PaloTAbajoVertical_gemela = crearPared(322,527,28,69)
        listaParedes.add(PaloTAbajoVertical_gemela)
        spritesDelJuego.add(PaloTAbajoVertical_gemela)

        paloHorizontalPequenio_abajoDer = crearPared(396,454,96,19)
        listaParedes.add(paloHorizontalPequenio_abajoDer)
        spritesDelJuego.add(paloHorizontalPequenio_abajoDer)

        paloHorizontalPequenio_abajoIzq = crearPared(178,454,97,19)
        listaParedes.add(paloHorizontalPequenio_abajoIzq)
        spritesDelJuego.add(paloHorizontalPequenio_abajoIzq)

        paloSalienteIzq = crearPared(5,515,53,23)
        listaParedes.add(paloSalienteIzq)
        spritesDelJuego.add(paloSalienteIzq)

        paloSalienteDer = crearPared(614,515,53,23)
        listaParedes.add(paloSalienteDer)
        spritesDelJuego.add(paloSalienteDer)

        paloLHorizontal_Izq = crearPared(60,451,72,23)
        listaParedes.add(paloLHorizontal_Izq)
        spritesDelJuego.add(paloLHorizontal_Izq)

        paloLVertical_Izq = crearPared(104,463,28,73)
        listaParedes.add(paloLVertical_Izq)
        spritesDelJuego.add(paloLVertical_Izq)

        paloLHorizontal_Der = crearPared(539,451,72,23)
        listaParedes.add(paloLHorizontal_Der)
        spritesDelJuego.add(paloLHorizontal_Der)

        paloLVertical_Der = crearPared(539,463,28,73)
        listaParedes.add(paloLVertical_Der)
        spritesDelJuego.add(paloLVertical_Der)

        paloTBocaAbajoHorizontal_Izq = crearPared(60,579,214,22)
        listaParedes.add(paloTBocaAbajoHorizontal_Izq)
        spritesDelJuego.add(paloTBocaAbajoHorizontal_Izq)

        paloTBocaAbajoVertical_Izq = crearPared(177,520,30,71)
        listaParedes.add(paloTBocaAbajoVertical_Izq)
        spritesDelJuego.add(paloTBocaAbajoVertical_Izq)

        paloTBocaAbajoHorizontal_Der = crearPared(398,579,214,22)
        listaParedes.add(paloTBocaAbajoHorizontal_Der)
        spritesDelJuego.add(paloTBocaAbajoHorizontal_Der)

        paloTBocaAbajoVertical_Der = crearPared(466,520,30,71)
        listaParedes.add(paloTBocaAbajoVertical_Der)
        spritesDelJuego.add(paloTBocaAbajoVertical_Der)

        return listaParedes

    '''THIS FUNCTION IS TO SHOW ON THE SCREEN THAT PACMAN LOST'''
    def gameOver(pantalla):
        pantalla.fill((128,0,128))

        gameOver_texto = pygame.font.Font(None, 50).render("Game Over, PRESS [Q] to finish.", True, (0,0,255))
        text_rect = gameOver_texto.get_rect()
        text_rect.center = (ANCHO_PANTALLA // 2, LARGO_PANTALLA // 2)
        pantalla.blit(gameOver_texto, text_rect)

    '''THIS FUNCTION IS TO SHOW ON THE SCREEN THAT PACMAN WON'''
    def youWin(pantalla):
        pantalla.fill((128,0,128))

        youWin_texto = pygame.font.Font(None, 50).render("You Win!!!, PRESS [Q] to finish.", True, (0,0,255))
        text_rect = youWin_texto.get_rect()
        text_rect.center = (ANCHO_PANTALLA // 2, LARGO_PANTALLA // 2)
        pantalla.blit(youWin_texto, text_rect)

    #This function 
    def gestionarEventos(protagonista, isRunning):
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                isRunning = False
            if evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_a)or(evento.key == pygame.K_LEFT):
                    protagonista.velocidad_x = -2
                    protagonista.velocidad_y = 0
                elif (evento.key == pygame.K_d)or(evento.key == pygame.K_RIGHT):
                    protagonista.velocidad_x = 2
                    protagonista.velocidad_y = 0
                elif (evento.key == pygame.K_w)or(evento.key == pygame.K_UP):
                    protagonista.velocidad_y = -2
                    protagonista.velocidad_x = 0
                elif (evento.key == pygame.K_s)or(evento.key == pygame.K_DOWN):
                    protagonista.velocidad_y = 2
                    protagonista.velocidad_x = 0
                elif evento.key == pygame.K_q:
                    isRunning = False
        return isRunning

    '''VARIABLES ARE CREATED AND THE FUNCTIONS ARE CALLED SO THE DIFFERENT ACTIONS ARE EXECUTED'''
    pygame.init()

    PUNTOS = 0
    VIDAS = 3
    contador = 0


    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,LARGO_PANTALLA])

    pygame.display.set_caption("Pac-Man")

    spritesDelJuego = pygame.sprite.Group()

    spritesProtagonista = pygame.sprite.Group()

    spritesFantasma = pygame.sprite.Group()

    protagonista = crearProtagonista(spritesProtagonista)

    listaBolas = createBolas(spritesDelJuego)

    listaFrutas = createFrutaEspecial(spritesDelJuego)

    fantasmaAzul = crearFantasmaAzul(spritesFantasma)

    fantasmaRosa = crearFantasmaRosa(spritesFantasma)

    fantasmaRojo = crearFantasmaRojo(spritesFantasma)

    fantasmaNaranja = crearFantasmaNaranja(spritesFantasma)

    listaParedes = createParedes(spritesDelJuego)

    reloj = pygame.time.Clock()

    pygame.display.update()

    isRunning = True
    while isRunning:
        
        isRunning = gestionarEventos(protagonista, isRunning)

        for evento in pygame.event.get():
            if (evento.type == pygame.KEYDOWN):
                if  evento.key == pygame.K_q:
                    isRunning = False
            elif evento.type == pygame.QUIT:
                isRunning = False

        updateProtagonista(protagonista, listaParedes)
        aparecerLadoContrario(protagonista)
        
        pygame.display.update()

        background_image = pygame.image.load("Imagenes\PacmanStage.png")
        
        pantalla.blit(background_image,(0, 0))

        spritesDelJuego.draw(pantalla)

        spritesProtagonista.draw(pantalla)

        spritesFantasma.draw(pantalla)

        PUNTOS, c = colisionBolas(protagonista, listaBolas, PUNTOS)
        
        if colisionFantasmasPacmanVidaMenos(protagonista, fantasmaAzul) or colisionFantasmasPacmanVidaMenos(protagonista, fantasmaRosa) or colisionFantasmasPacmanVidaMenos(protagonista, fantasmaRojo) or colisionFantasmasPacmanVidaMenos(protagonista, fantasmaNaranja):
            VIDAS = VIDAS - 1
        
        if VIDAS == 0:
            gameOver(pantalla)
            fantasmaAzul.velocidad_x = 0
            fantasmaAzul.velocidad_y = 0
            fantasmaAzul.rect.x = 262
            fantasmaAzul.rect.y = 292
            fantasmaRosa.velocidad_x = 0
            fantasmaRosa.velocidad_y = 0
            fantasmaRosa.rect.x = 295
            fantasmaRosa.rect.y = 292
            fantasmaRojo.velocidad_x = 0
            fantasmaRojo.velocidad_y = 0
            fantasmaRojo.rect.x = 295
            fantasmaRojo.rect.y = 292
            fantasmaNaranja.velocidad_x = 0
            fantasmaNaranja.velocidad_y = 0
            fantasmaNaranja.rect.x = 295
            fantasmaNaranja.rect.y = 292
            protagonista.velocidad_x = 0
            protagonista.velocidad_y = 0
        
        if PUNTOS == 4200:
            youWin(pantalla)
            fantasmaAzul.velocidad_x = 0
            fantasmaAzul.velocidad_y = 0
            fantasmaAzul.rect.x = 262
            fantasmaAzul.rect.y = 292
            fantasmaRosa.velocidad_x = 0
            fantasmaRosa.velocidad_y = 0
            fantasmaRosa.rect.x = 295
            fantasmaRosa.rect.y = 292
            fantasmaRojo.velocidad_x = 0
            fantasmaRojo.velocidad_y = 0
            fantasmaRojo.rect.x = 295
            fantasmaRojo.rect.y = 292
            fantasmaNaranja.velocidad_x = 0
            fantasmaNaranja.velocidad_y = 0
            fantasmaNaranja.rect.x = 295
            fantasmaNaranja.rect.y = 292
            protagonista.velocidad_x = 0
            protagonista.velocidad_y = 0


        colisionFrutas(protagonista, listaFrutas)

        puntuacion(pantalla, PUNTOS)

        mostrarVidas(pantalla, VIDAS)

        updateFantasmas(fantasmaAzul, listaParedes)
        aparecerLadoContrario(fantasmaAzul)
        salirJaulaFantasma(fantasmaAzul)

        updateFantasmas(fantasmaRosa, listaParedes)
        aparecerLadoContrario(fantasmaRosa)
        salirJaulaFantasma(fantasmaRosa)

        updateFantasmas(fantasmaRojo, listaParedes)
        aparecerLadoContrario(fantasmaRojo)
        salirJaulaFantasma(fantasmaRojo)

        updateFantasmas(fantasmaNaranja, listaParedes)
        aparecerLadoContrario(fantasmaNaranja)
        salirJaulaFantasma(fantasmaNaranja)

        

        pygame.display.flip()

        reloj.tick(30)

        await asyncio.sleep(0)

asyncio.run(main())



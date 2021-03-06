#!/usr/env/bin python3
import pygame
import os
from time import sleep
from random import randint
from superpyboy.player import Player
from superpyboy.enemy import Enemy

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'images')
player = os.path.join(resource_path, 'players')
elements = os.path.join(resource_path, 'elements')
background = os.path.join(resource_path, 'background')
ennemies = os.path.join(resource_path, 'ennemies')

class Window(object):


    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height

        pygame.init()

        #Titre de la fenêtre
        pygame.display.set_caption("SCORPI")

        #Taille de la fenêtre
        self._window = pygame.display.set_mode((self.width, self.height))



        self.enne = pygame.image.load(os.path.join(ennemies, "snail.png")).convert_alpha()
        self._window.blit(self.enne, (self.width - 250, (self.height - 70) - self.enne.get_size()[1]))
        self.ennemy = Enemy(self.width - 250, ((self.height - 70) - self.enne.get_size()[1]))

        self.drawScreen()

        pinkPlayer = pygame.image.load(os.path.join(player, "player-right.png")).convert_alpha()
        self._window.blit(pinkPlayer, (0, (self.height - 70) - pinkPlayer.get_size()[1]))
        self.player = Player("L", 0, ((self.height - 70) - pinkPlayer.get_size()[1]))

        pygame.display.flip()
        pygame.key.set_repeat(400,30)
        #self.enemies = [Enemy('foo', Enemy("bar")]

    def run(self):
        running = True
        while running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    keystate = pygame.key.get_pressed()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False

                        self.player.update(event)

                        newPlayer = pygame.image.load(os.path.join(player, "player-right.png")).convert_alpha()
                        if (event.key == pygame.K_LEFT):
                            newPlayer = pygame.transform.flip(newPlayer, True, False)

                        if not self.player.x < 0 or self.player.x > self.width - newPlayer.get_size()[0]:
                            self.drawScreen()
                            self._window.blit(newPlayer, (self.player.x, self.player.y))


                        #DETECT COLLISION
                        rectPlayer = pygame.Rect(self.player.x, self.player.y, 70, 70)
                        rectEnemy = pygame.Rect(self.ennemy.x, self.ennemy.y, 70, 70)

                        if rectPlayer.colliderect(rectEnemy):
                            pygame.font.init()
                            myfont = pygame.font.SysFont('Comic Sans MS', 100)
                            textsurface = myfont.render('GAME OVER', False, (0, 0, 0))
                            self._window.blit(textsurface, (self.width / 4, self.height / 4 ))
                            pygame.display.flip()
                            sleep(0.5)
                            self.__init__()

                        pygame.display.flip()

                    elif keystate[pygame.K_UP]:
                        print(event)
                        print("pressed up")



    def drawScreen(self):

        # Chargement de l'image
        desertBackground = pygame.image.load(os.path.join(background, "bg_desert.png")).convert_alpha()
        desertBackground = pygame.transform.scale(desertBackground, (self.width, self.height))

        floorLeft = pygame.image.load(os.path.join(elements, "cakeLeft.png")).convert_alpha()
        floorMid = pygame.image.load(os.path.join(elements, "cakeMid.png")).convert_alpha()
        floorRight = pygame.image.load(os.path.join(elements, "cakeRight.png")).convert_alpha()

        # positionPlayer = pinkPlayer.get_rect()

        # Ajout de l'image sur la fenêtre
        self._window.blit(desertBackground, [0, 0])

        # Ajout du premier bloc sur la gauche
        self._window.blit(floorLeft, (0, self.height - floorLeft.get_size()[1]))

        # Nombre de bloc que l'on peut mettre en fonction de la largeur de l'écran
        nb = int(self.width / floorMid.get_size()[1])
        randomNb = 5 #randint(2, nb - 2)

        for x in range(0, nb):
            if x - 1 == randomNb:
                self._window.blit(floorLeft, (70 * x, self.height - floorLeft.get_size()[1]))
            elif x + 1 == randomNb:
                self._window.blit(floorRight, (70 * x, self.height - floorRight.get_size()[1]))
            elif x != randomNb:
                self._window.blit(floorMid, (70 * x, self.height - floorMid.get_size()[1]))

        self._window.blit(self.enne, (self.ennemy.x, self.ennemy.y))
       # Ajout du dernier bloc sur la droite
        self._window.blit(floorRight, (self.width - floorRight.get_size()[0], self.height - floorRight.get_size()[1]))

        # Rafraîchissement de l'écran
        pygame.display.flip()

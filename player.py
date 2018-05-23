#!/usr/env/bin python3

import pygame

class Player(object):

    image_standing = 'images/player-default.png'
    image_right = 'images/player-right.png'
    image_left = 'images/player-left.png'


    v = 8
    m = 2


    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.isjump = False
        self.jumpCount = 10


    def move_x(self, value):
        # Other stuff like checking if you are running into a wall
        self.x += value
        if self.x < 0:
            self.x = 0
        elif self.x >= 810:
            self.x = 810




    def move_y(self, value):
        # Other stuff like checking if you a stopped by a plateform in you fall.
        #self.y += value
        # Calculate force (F). F = 0.5 * mass * velocity^2.
        if value > 0:
            print("down!")
        elif value < 0:
            if self.v > 0:
                F = (0.5 * self.m * (self.v * self.v))
            else:
                F = -(0.5 * self.m * (self.v * self.v))
        
                    # Change position
            self.y = self.y - F
        
                    # Change velocity
            self.v = self.v - 1
        
                    # If ground is reached, reset variables.
            if self.y >= 500:
                self.y = 500
                self.v = 8

    def update(self, event):
        if event.key == pygame.K_LEFT:
            self.move_x(-20)
        elif event.key == pygame.K_RIGHT:
            self.move_x(20)
        elif event.key == pygame.K_UP:
            self.move_y(-50)
        elif event.key == pygame.K_DOWN:
            self.fall()

    def jump(self):
        print("jump")

        if self.v > 0:
            F = (0.5 * self.m * (self.v * self.v))
        else:
            F = -(0.5 * self.m * (self.v * self.v))

            # Change position
        self.y = self.y - F

            # Change velocity
        self.v = self.v - 1

            # If ground is reached, reset variables.
        if self.y >= 435:
            self.y = 435
            self.isjump = 0
            self.v = 8



    def fall(self):

        print("fall")
        self.move_y(+80)

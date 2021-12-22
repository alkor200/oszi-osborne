import sys

import pygame

from pygame.locals import *


class GamePad:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            print(joystick.get_name())

    def get_event(self):
        for event in pygame.event.get():
            if event.type == JOYBUTTONDOWN:
                print(event)
            if event.type == JOYBUTTONUP:
                print(event)
            if event.type == JOYAXISMOTION:
                print(event)
            if event.type == JOYHATMOTION:
                print(event)
            if event.type == JOYDEVICEADDED:
                self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in self.joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

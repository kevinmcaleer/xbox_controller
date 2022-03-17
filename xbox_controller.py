import pygame
from pygame.constants import JOYBUTTONDOWN, KEYDOWN
pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

print(joysticks)

while True or KeyboardInterrupt:
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0
                print("button down")∏
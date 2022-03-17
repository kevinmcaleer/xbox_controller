

import pygame
from pygame.constants import JOYBUTTONDOWN
pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

print(joysticks)
print(pygame.joystick.Joystick(0).get_name())

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

while True or KeyboardInterrupt:
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0:
                print("button 0 down")
            if event.button == 1:
                print("button 1 down")
            if event.button == 2:
                print("button 2 down")
            if event.button == 3:
                print("button 4 down")
            if event.button == 5:
                print("button 5 down")
            if event.button == 6:
                print("button 6 down")
            if event.button == 7:
                print("button 7 down")
            if event.button == 8:
                print("button 8 down")
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2: # Left stick
                print(f"motion axis:value {event.value}")
                if event.axis == 0: # up/down
                    if event.value < 0:
                        print("down")
                    if event.value > 0:
                        print("up")
                if event.axis == 1: # left/right
                    if event.value < 0:
                        print("left")
                    if event.value > 0:
                        print("right")
            # print(event)
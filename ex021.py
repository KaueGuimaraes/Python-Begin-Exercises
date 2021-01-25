import pygame

pygame.init()
pygame.mixer.music.load('audioex020.mp3')
pygame.mixer.music.play()
pygame.event.wait()
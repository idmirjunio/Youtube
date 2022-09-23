import pygame
pygame.mixer.pre_init(channels=8)
pygame.init()
a=pygame.mixer.get_num_channels()
print(a)
print(type(a))


pygame.mixer.music.load("C:/Users\ccsst\OneDrive\Área de Trabalho\python\controller MIDI\Rap do Satoru Gojo_ Mundo Infinito (feat. Leo0Machado)_160k.mp3")
pygame.mixer.music.play()
input()
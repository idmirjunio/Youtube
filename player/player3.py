
#import pygame

#pygame.init()
#c= mixer.get_num_channels()
#pc = mixer.find_channel()
#v= mixer.get_busy()
#pygame.mixer.music.load("D:/vscode\python\player\ex21.mp3")
#pygame.mixer.music.play()
#pygame.event.wait()
#print(c)
#print(pc)
#print(v)
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('D:/vscode\python\player\ex21.mp3')
pygame.mixer.music.play()
print("ok")
i = "toque"
while i == "sair":
 if i == "pause":
   pygame.mixer.music.pause
 elif i == "continuar":
     pygame.mixer.music.unpause    
 i= input(":")
#x=input()
#pygame.mixer.music.load('D:/vscode\python\player\ex22.mp3')
#pygame.mixer.music.play()
#x=input()
#import time
#time.sleep(360)
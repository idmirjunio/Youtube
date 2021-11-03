import random
from time import sleep
print("escolha sua jogada:  ")
print("[0]pedra")
print("[1]papel")
print("[2]tesoura")
jogador = int(input())
sleep(0.3)
print("JO")
sleep(0.3)
print("KEN")
sleep(0.3)
print("PO")

opcao=random.randint(0,2)
itens=("pedra","papel", "tesoura")

print("O pc jogou {}, ".format(itens[opcao]))
print("Você jogou {}, ".format(itens[jogador]))
ind= opcao - 1 
if ind == -1: ind = 2
if opcao== jogador:
    print("Ouve impate!")

elif ind == jogador:
    print("Você Perdeu!")
else:
      print("Você Ganhou!")   

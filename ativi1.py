import math
nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.title()
v1 = nome.find(" ")
v2 = nome.rfind(" ")
print("Seu primeiro nome é {}, seu ultimo nome {}".format(nome[:v1+1],nome[v2+1:]))

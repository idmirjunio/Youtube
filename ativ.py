import random
a = str(input("Digie um numero com até 4 algarismos: "))
a = a.zfill(4) 
uni=a[3:]
dez=a[2:3]
cen=a[1:2]
mi=a[:1]
print("O numero {}".format(a))
print("Unidade: {}".format(uni))
print("Dezena: {}".format(dez))
print("Centena: {}".format(cen))
print("Milhar: {}".format(mi))
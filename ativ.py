
a = int(input("Digite o Primerio segmento  "))
b = int(input("Digite o Segundo segmento  "))
c = int(input("Digite o terceiro segmento  "))

if a+b>c and b+c>a and c+a>b:
    if a==b==c:
       print("Esses segmentos formam um triangulo EQUILATERO") 
    elif a==b or b==c or a==c :
      print("Esses segmentos formam um triangulo ISOSCELES")     
    elif a!=b!=c!=a:
          print("Esses segmentos formam um triangulo ESCALENO")   
else:
  print("Esses segmentos NÃO formam um triângulo!")


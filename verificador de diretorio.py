def adicionar_diretorio(nome):
 import json
 from index import cruzador

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()

 data = cruzador.data_atual() 

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","w")

 y.update({nome:data})

 json.dump(y,x)

 x.close()   

def pesquisar_diretorio(nome):
 import json
 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()
 cod = False   
 for l in y:
  if l == nome:
            cod = True  
            return True 
        
 if cod == False:
   return False    


def analisar_biblioteca():
 import os 
 

 dir= "D:/biblioteca"
 diretorio= "D:/vscode/python/arquivos_temp/diretorio.json"
 for a in os.listdir(dir):
      if a.endswith(".mp4"):
       v= a.find(".mp4")
       if v != -1:
        nome = a[0:v]   
        ret = pesquisar_diretorio(nome=nome)
        if ret == False:
          adicionar_diretorio(nome)     
          
        
analisar_biblioteca() 

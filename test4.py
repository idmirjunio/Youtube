
import json
nome = "docijdoijcoij"
data = "isisikj"

try:
  v = open(r"D:\vscode\python\arquivos_temp\diretorio.json","x")

  v.write('{"nome":"data"}')
   
  v.close() 
except:pass

    
x = open(r"D:\vscode\python\arquivos_temp\diretorio.json","r")

y = json.load(x)

x.close()

x = open(r"D:\vscode\python\arquivos_temp\diretorio.json","w")

y.update({nome:data})

json.dump(y,x,indent=4)

x.close()

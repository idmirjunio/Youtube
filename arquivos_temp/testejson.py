import json

x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

y = json.load(x)

x.close()

x = open("D:/vscode/python/arquivos_temp/bibliotec.json","w")

y.update({"colo": "loa"})

json.dump(y,x)

x.close()



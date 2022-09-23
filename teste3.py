from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

#win32clipboard.OpenClipboard()
#link = win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()

link = ("https://youtu.be/QDLVSyBQHDU?list=RDGyroith0-Rc")



def saber_res(resolucao,formato,ada,progress,tipo, ):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(res=resolucao, file_extension=formato,adaptive=ada,progressive=progress,type=tipo))

 yt = yt.strip("[]")

 yt = yt.replace("<","")

 yt = yt.replace(">","")

 list = yt.split(",")


 for a in range(0,len(list)):

     list[a] = list[a].strip()


 dic = [0]
 dic[0] = list[0].split()

 for a in range(1,len(list)):

  dic.insert(a,list[a].split())

 res_max ="0"
 res_atual = "0"
 for a in range(0,len(dic)):
   tamanho_dic2 = len(dic[a])

   for b in range(0,tamanho_dic2):  
    verificar_res = dic[a][b].startswith("res")
    if verificar_res == True :
     frase = dic[a][b]
     res_max = res_max.zfill(4)
     res_atual = res_atual.zfill(4)
     #print(res_atual)
     if res_atual > res_max:
       res_max = res_atual 

     res_atual = ""
     for c in range(0,len(frase)):
           ind = frase[c].isnumeric()
           if ind == True:
               res_atual = res_atual + frase[c]
                




#x = x.replace(",","")
#list[a] 


from logging import ERROR

from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

#win32clipboard.OpenClipboard()
#link = win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()


link = ("https://youtu.be/QDLVSyBQHDU?list=RDGyroith0-Rc")
def pegar_itag() :#resolucao,formato,adaptive,progressive,tipo):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(res="1080p"))#res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo))

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

 list_c = []
 l = 0  
 for a in range(0,len(dic)):
   tamanho_dic2 = len(dic[a])

   for b in range(0,tamanho_dic2):
        
    verificar_codec = dic[a][b].startswith("vcodec")
    if verificar_codec == True :
     list_c.insert(l,dic[a][b])
     l = l + 1  
 cod1 = 0 # av01
 cod2 = 0 # vp9
 cod3 = 0 # avc
 cod4 = 0 # mp4    
 for c in range(0, len(list_c)): 
     codec = ""
     frase = list_c[c]   
     v1 = frase.find('"')
     v2 = frase.rfind('"')
     for c in range(v1+1,v2):
        codec = codec + frase[c]
     
       
     if codec[0] == "a" and codec[1] == "v" and codec[2] != "c":
      cod1=cod1+1
     if codec[0] == "v" and codec[1] == "p" and codec[2] == "9":
      cod2=cod2+1 
     if codec[0] == "a" and codec[1] == "v" and codec[2] == "c":
      cod3=cod3+1 
     if codec[0] == "m" and codec[1] == "p" and codec[2] == "4":
      cod4=cod4+1 

 if cod1+cod2+cod3+cod4 != len(list_c):
  print(cod1)
  print(cod2)
  print(cod3)
  print(len(list_c))
  print(list_c) # exibir aviso(ERROR!)
 else: 
         if cod1 == 1: 
            codecv_= "av0"
            
         else: 
              if cod2 == 1: 
                 codecv_= "vp9"
              else:
                   if cod3 == 1: 
                      codecv_= "avc"
                   else:
                       if cod4 == 1: 
                          codecv_= "mp4"

         if cod1 < 1: pass # (ERROR)
         if cod1 == 0: pass
         
         if cod2 < 1: pass # (ERROR)
         if cod2 == 0: pass 
        
         if cod3 < 1: pass#(ERROR)
         if cod3 == 0: pass#(ERROR)
                      
 for d in range(0, len(list_c)): 
     codec = list_c[d]
     ind =codec.find('"')
     v=codec.startswith(codecv_,ind+1)          
     if v == True:
      parc = d    
      break
 for e in range(0, len(dic[parc])):
     var_encontra = dic[parc][e]
     bin = var_encontra.find('itag')
     if bin != -1:
        c1 = var_encontra.find('"')
        c2 = var_encontra.rfind('"')
        valor_itag = var_encontra[c1+1:c2]
        break
 return str(valor_itag)
         
          


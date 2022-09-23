



from pytube import YouTube, Channel, Playlist
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()                
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


    


def transformar(url):
 ind=1
 stream={"Stream1":{} }
 for g in range(len(url)):
  local= "Stream"+str(ind)


  a= str(url[g])
  b=a.strip("<>").replace('=',' ').replace('"','').replace("/"," format ").split(" ")
 
  del b[0]

  if ind != 1:
      stream[local]={}
  for i in range(0,len(b),2):
   j= i+1
  
   stream[local][b[i]]=b[j]
  
   j=0
  ind = ind+1 
 for i in stream:
  try:   
   m=stream[i]["fps"]
   for h in m : 
    if h.isalpha()==True:
       m=m.replace(h,"") 
   stream[i]["value_fps"]=int(m)
  except:  
    pass

 for i in stream:
  try:   
   m=stream[i]["res"]
   for h in m : 
    if h.isalpha()==True:
       m=m.replace(h,"") 
   stream[i]["resolution"]=int(m)
  except:  pass
   
 for i in stream:
  try:   
   m=stream[i]["abr"]
   for h in m : 
    if h.isalpha()==True:
       m=m.replace(h,"") 
   stream[i]["abr_value "]=int(m)
  except:  pass
  return stream


def data_atual():
 from datetime import datetime

 # datetime object containing current date and time
 now = datetime.now()


 # dd/mm/YY H:M:S
 dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 return dt_string


def adicionar_biblioteca_json(nome):
 import json

 try:
  v = open(r"D:\vscode\python\arquivos_temp\bibliotec.json","x")

  v.write('{"nome":"data"}')
   
  v.close() 
 except:pass

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()

 data = data_atual() 

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","w")

 y.update({nome:data})

 json.dump(y,x,indent=4)

 x.close()
    

def melhor_kbps(resolucao,formato,adaptive,progressive,tipo):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo))

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

 abr=[]
 l = 0  
 for a in range(0,len(dic)):
   tamanho_dic2 = len(dic[a])

   for b in range(0,tamanho_dic2):
        
    verificar_abr = dic[a][b].startswith("abr")
    if verificar_abr == True :
      abr.insert(l,dic[a][b])
      l = l+1
 num_list = []
 buff_list = ""   
 for c in range(0,len(abr)):
    kbps_n = abr[c]
    if buff_list != "":
      buff_complet=buff_list.zfill(4)  
      num_list.insert(c,buff_complet)      
    buff_list = ""
    for d in range(0,len(kbps_n)):
            ind = kbps_n[d]
            loc= ind.isnumeric()
            if loc == True:
             buff_list = buff_list + ind
 k_max = "0000"            
 for e in range(0, len(num_list)):
     
     k_atual = num_list[e]
     if k_atual > k_max:
         k_max = k_atual
 abr_max = k_max.lstrip("0")
 abr_max = abr_max + "kbps"                     
 return abr_max



def verificar_codec(resolucao,formato,adaptive,progressive,tipo):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo))

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


def saber_res(resolucao=None,formato=None,adaptive=None,progressive=None,tipo=None,maior_720=False ):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo))

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
     if res_atual > res_max:
       res_max = res_atual 

     res_atual = ""
     for c in range(0,len(frase)):
           ind = frase[c].isnumeric()
           if ind == True:
               res_atual = res_atual + frase[c]
 if maior_720 == True:
      if res_max <= "0720":
            res_max = "0000" 
            return res_max
      else:
        return res_max +"p"      
 else:
     return res_max +"p"




def pegar_itag(resolucao=None,formato=None,adaptive=None,progressive=None,tipo=None,abr=None):
 yt = YouTube(link, on_progress_callback = on_progress)

 
 yt = str(yt.streams.filter(res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo,abr=abr))

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

 
 for a in range(0,len(dic)):
   tamanho_dic2 = len(dic[a])

   for b in range(0,tamanho_dic2):  
    verificar_itag = dic[a][b].startswith("itag")
    if verificar_itag == True :
     frase = dic[a][b]
     itag = ""
     for c in range(0,len(frase)):
           ind = frase[c].isnumeric()
           if ind == True:
               itag = itag + frase[c]
 print(itag)              
 return itag              





          











#funcao
def audio_adaptive_Formato_opus(kbps):
    
 x=yt.streams.filter(type="audio",adaptive=True,file_extension='opus')#melhor audio
 # se len(x) == 0 entao ERROR (Filtro não possui valor classificado, n é nem mp4 ou opus  Res: possivel novo formato de audio do pytube ou YouTube) 
 if len(x) == 1: 
   itag = pegar_itag(adaptive= False,tipo="audio",resolucao= 0,formato="opus",abr=kbps)
   x = yt.streams.get_by_itag(itag)
   x.download(output_path="D:/biblioteca(mxxx)")
   name= yt.title
   adicionar_biblioteca_json(name)
 # se len(x) > 2  verificar codec

#funcao
def audio_adaptive_Formato_mp4(kbps):
    
 x=yt.streams.filter(type="audio",adaptive=True,file_extension='mp4',abr=kbps)#melhor audio
 if len(x) == 0 : audio_adaptive_Formato_opus(kbps=kbps)#melhor audio
 else:
  if len(x) == 1 :
   itag = pegar_itag(adaptive= False,tipo="audio",resolucao= 0,formato="mp4",abr=kbps)
   x = yt.streams.get_by_itag(itag)
   x.download(output_path="D:/biblioteca(mxxx)")
   name= yt.title
   adicionar_biblioteca_json(name)
 # se len(x) > 2 verificar codec

#funcao
def audio_adaptive():     
 kbps = melhor_kbps(resolucao=0,formato="",adaptive=False,progressive=False,tipo="audio")   
 x=yt.streams.filter(type="audio",adaptive=True,abr=kbps)#melhor audio
 # se len(x) == 0 entao ERROR (valor de #melhor audio inesperado ou inexistente Res: Verificar Stream e codigo-fonte)
 if len(x) == 1 :
   itag = pegar_itag(adaptive= False,tipo="audio",resolucao= 0,formato="",abr=kbps,progressive=False)
   x = yt.streams.get_by_itag(itag) 
                               
   x.download(output_path="D:/biblioteca(mxxx)")
   name= yt.title
   adicionar_biblioteca_json(name)
 else:      
  if len(x) > 2 : audio_adaptive_Formato_mp4(kbps=kbps)#melhor audio 
                                        



try:
 yt=YouTube(link)
 audio_adaptive()
except:  
 try:
   yt = Playlist(link)
   for link in yt.video_urls:
    yt = YouTube(link).streams
    audio_adaptive()   
   
    
 except:
   try:
    yt = Channel(link)
    for url in yt.video_urls:
     yt = YouTube(url).streams.fmt_streams
     stream=transformar(url=yt)
   
   except: 
    exit()   
  
import pytube
import atributos


from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
print(link)
win32clipboard.CloseClipboard()


t = link.find("youtu.be")
l = link.find("youtube")
print(l)
if t == -1:
    

 if l == -1:
    exit()     
#link = ("https://youtu.be/Gyroith0-Rc?list=RDGyroith0-Rc")
#link = ("https://youtu.be/jfLHgN_1dLU")
yt = YouTube(link,on_progress_callback = on_progress)


x = yt.streams.filter(progressive=True)

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


def saber_res(resolucao,formato,adaptive,progressive,tipo,maior_720 ):
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




def pegar_itag(resolucao,formato,adaptive,progressive,tipo,abr):
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
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="audio",formato=".webm")
 # se len(x) > 2  verificar codec

#funcao
def audio_adaptive_Formato_mp4(kbps):
    
 x=yt.streams.filter(type="audio",adaptive=True,file_extension='mp4',abr=kbps)#melhor audio
 if len(x) == 0 : audio_adaptive_Formato_opus(kbps=kbps)#melhor audio
 else:
  if len(x) == 1 :
   itag = pegar_itag(adaptive= False,tipo="audio",resolucao= 0,formato="mp4",abr=kbps)
   x = yt.streams.get_by_itag(itag)
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="audio",formato=".mp4")
 # se len(x) > 2 verificar codec

#funcao
def audio_adaptive():      #\MODIFICADO1111111111111111111111111
 kbps = melhor_kbps(resolucao=0,formato="",adaptive=False,progressive=False,tipo="audio")   
 x=yt.streams.filter(type="audio",adaptive=True,abr=kbps)#melhor audio
 # se len(x) == 0 entao ERROR (valor de #melhor audio inesperado ou inexistente Res: Verificar Stream e codigo-fonte)
 if len(x) == 1 :
   itag = pegar_itag(adaptive= False,tipo="audio",resolucao= 0,formato="",abr=kbps,progressive=False)
   x = yt.streams.get_by_itag(itag)                              #\modificado!!!!!!!!!!!!!!!!
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="audio")
 else:      
  if len(x) > 2 : audio_adaptive_Formato_mp4(kbps=kbps)#melhor audio 
                                        
#funcao
def adaptive_true_Type_audio():
    
 x=yt.streams.filter(type="audio",adaptive=True)
 if len(x) > 0: audio_adaptive()
 #senao entao(registrar)




#funcao
def adaptive_True_Type_video_file_webm_res_max(p):
 x=yt.streams.filter(type="video",adaptive=True,file_extension='webm',res=p)#+maior resolução
 if len(x) == 1 :
   itag = pegar_itag(adaptive= True,tipo="video",resolucao=p,formato="webm",abr="",progressive=False)
   x = yt.streams.get_by_itag(itag)
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="video",formato=".webm")
   adaptive_true_Type_audio()     
 else:  
  # se len(x) == 0 (A stream é adaptive=true, #maior resolução, nao é mp4 nem webm; Res: Formato diferente de mp4 e webm )
  if len(x) > 2: 
   codec = verificar_codec(progressive=False,formato="webm",adaptive=True,resolucao=p,tipo="video")
   x = yt.streams.get_by_itag(codec)
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="video")
   adaptive_true_Type_audio()
       #verificar codec

#funcao
def adaptive_True_Type_video_file_mp4_res_max(p):
   
 x=yt.streams.filter(type="video",adaptive=True,file_extension='mp4',res=p)#+maior resolução
 if len(x) == 1 :  
   itag = pegar_itag(adaptive= True,tipo="video",resolucao=p,formato="mp4",abr="")
   x = yt.streams.get_by_itag(itag)
   x.download()
   atributos.enviar_para_cruzamento(link=link,tipo="video")
   adaptive_true_Type_audio()
 else:  
  if len(x) == 0: adaptive_True_Type_video_file_webm_res_max(p=p) #funcao (type="video",adaptive=True,file_extension='webm')#+maior resolução)
  else:
   if len(x) <= 2 : 
    codec = verificar_codec(progressive=False,formato="mp4",adaptive=True,resolucao=p,tipo="video")
    x = yt.streams.get_by_itag(codec)
    x.download()
    atributos.enviar_para_cruzamento(link=link,tipo="video")
    adaptive_true_Type_audio()

#funcao
def adaptive_True_Type_video_Res_max():
 p = saber_res(adaptive=True,tipo="video",resolucao="",formato="",progressive="",maior_720=False)
 x=yt.streams.filter(type="video",adaptive=True,res=p)#+maior resolução
 if len(x) == 1 :     
  itag = pegar_itag(adaptive= True,tipo="video",resolucao=p,abr="")
  x = yt.streams.get_by_itag(itag)
  x.download()
  atributos.enviar_para_cruzamento(link=link,tipo="video")
  adaptive_true_Type_audio()
 # se len(x) == 0 entao ERROR (A funçao Achar_maior_resolucao retornou um valor inexistente; Res: Modificação da forma de retorno da Stream no pytube ou YouTube)
 else:
  if len(x) > 2 :
   adaptive_True_Type_video_file_mp4_res_max(p=p) #funcao (type="video",adaptive=True,file_extension='mp4')#+maior resolução
#\FOI MODIFICADO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#funcao
def adaptive_True_Type_video():
    
 x=yt.streams.filter(type="video",adaptive=True)
 if len(x) > 0 : adaptive_True_Type_video_Res_max() #função (type="video",adaptive=True)#+maior resolução
 #senao entao(registrar)
 #  

#funçao 
def progressive_True_file_webm_maior_q_720(p):
    
 x=yt.streams.filter(progressive=True,file_extension='webm',res=p)#resolucao<720p
 if len(x) == 1 : 
   x.download()
   atributos.enviar_para_biblioteca(link=link)
 # se len(x) > 2 entao funçao verificar codec
 # se len(x) == 0 entao ERROR (A stream é progressive=True, resolucao<720p, nao é mp4 nem webm; Res: Formato diferente de mp4 e webm )
 

#funçao 
def progressive_True_file_mp4_Res_maior_q_720(p):
    
 x=yt.streams.filter(progressive=True,file_extension='mp4',res=p)#resolucao<720p
 if len(x) == 1 :
       x.download()#avisar
       atributos.enviar_para_cruzamento(link=link)
 # se len(x) > 2 entao funçao verificar valor vcodec
 else:
  if len(x) == 0 : progressive_True_file_webm_maior_q_720(p=p) #funçao (progressive=True,file_extension='webm',res="1080p")


#funcao 
def progressive_true_Res_maior_q_720():
 p = saber_res(progressive = True,maior_720 = True,resolucao="",formato="",adaptive="",tipo="")
 x=yt.streams.filter(progressive=True,res=p)#resolucao<720p 
 if len(x) == 1 : pass #(listar feito com mensagem) 
 else:
  if len(x) == 0 : 
   adaptive_True_Type_video()   
  else:
   if len(x) > 2 :progressive_True_file_mp4_Res_maior_q_720(p=p)#(progressive=True,file_extension='mp4')#resolucao<720p 

x = yt.streams.filter(progressive=True)
#se len(x) > 0 entao funcao (progressive=True)#+maior resoluçao
if len(x) > 0: 
  progressive_true_Res_maior_q_720()

#caso nao entao (registra q n há video progressive)
# else:
#pass
#list = (yt.streams)

################################
#x = str(list[1])



#y = x.rsplit(" ")

#print(y)

 
#stream = '[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">,eam: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <S: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stretag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="399" mime_type="video/mp4" res="108ps="30fps" vcodec="av01.0.08M.08" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vc"avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressFalse" type="video">, <Stream: itag="398" mime_type="video/mp4" res="720p" fps="30fps" vcodec="av01.0.05M.08" progressive="False" type="">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: it44" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="397" mime_type="video/mes="480p" fps="30fps" vcodec="av01.0.04M.08" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fpsps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="396" mime_type="video/mp4" res="360p" fps="30fps" vcodec="av01.0.01M.08" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="395" mime_type="video/mp4" res="240p" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="394" mime_type="video/mp4" res="144p" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]'


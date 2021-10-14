from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

#win32clipboard.OpenClipboard()
#link = win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()


link = ("https://youtu.be/QDLVSyBQHDU?list=RDGyroith0-Rc")
def melhor_kbps() :#resolucao,formato,adaptive,progressive,tipo):
 yt = YouTube(link, on_progress_callback = on_progress)
 
 yt = str(yt.streams.filter(type="audio"))#res=resolucao, file_extension=formato,adaptive=adaptive,progressive=progressive,type=tipo))

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
# abr_max = abr_max.zfill(4)
# abr_atual = res_atual.zfill(4)
     #print(res_atual)
    # if res_atual > res_max:
    #   res_max = res_atual 

    # res_atual = ""
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
           #if ind == True:
             #  res_atual = res_atual + frase[c]
 k_max = "0000"            
 for e in range(0, len(num_list)):
     
     k_atual = num_list[e]
     if k_atual > k_max:
         k_max = k_atual
 abr_max = k_max.lstrip("0")
 abr_max = abr_max + "kbps"                      
 return abr_max
a=melhor_kbps() 
print(a)
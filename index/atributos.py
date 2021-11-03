from pytube import YouTube
import win32clipboard
import os
import cruzador

#win32clipboard.OpenClipboard()
#link = win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()

#link = ("https://www.youtube.com/watch?v=Gyroith0-Rc")
dir_path = "D:/vscode/python/"
fileDir= "D:/vscode/python"

def enviar_para_cruzamento(link,tipo,formato):
 
  if tipo == "video":   
   yt = YouTube(link).title
   file = yt+"(video)"
  
  else:
      if tipo == "audio": 
         yt = YouTube(link).title
         file = yt+"(audio)"
 
  for a in os.listdir(fileDir):
      if a.endswith(formato):
       os.rename(a,yt+formato)
  #dir_path = os.path.dirname(os.path.realpath(__file__))


  dest = "D:/vscode/python/arquivos_temp/"

  mac = cruzador.analisar_algo(yt)
  if mac == True:
      os.remove(dir_path+yt+formato)
       
  else:
   if mac == False:         
    os.rename(dir_path+yt+formato,dest+file+formato)

  if tipo == "audio" and mac == False: 
    try: 
     cruzador.unir_video_audio(nome=yt,formatovid= ".mp4",formatoaud=".mp4")
    except:
     try:   
      cruzador.unir_video_audio(nome=yt,formatovid= ".webm",formatoaud=".mp4") 
     except:
      try:   
       cruzador.unir_video_audio(nome=yt,formatovid= ".webm",formatoaud=".webm") 
      except:
       try:   
        cruzador.unir_video_audio(nome=yt,formatovid= ".mp4",formatoaud=".mp4") 
       except:
           print("chegou no fim e n executou!")   


        
#def saber_formato_video(nome):
    

#enviar_para_cruzamento(link=link,tipo="video")

def analisar_biblioteca():
 dir= "D:/biblioteca"
 diretorio= "D:\vscode\python\arquivos_temp\diretorio.json"
 for a in os.listdir(dir):
      if a.endswith(".mp4"):
       os.rename(a,yt+formato)
 os.rename(dir_path+yt+formato,dest+yt+formato)   
   


def enviar_para_biblioteca(link): 
 analisar_biblioteca()
 formato= ".mp4"

 yt = YouTube(link).title
 


 dest = "D:/biblioteca/"

 for a in os.listdir(fileDir):
      if a.endswith(".mp4"):
       os.rename(a,yt+formato)
 os.rename(dir_path+yt+formato,dest+yt+formato)   


def enviar_para_local(nome):
 #analisar_biblioteca()  
 dir_path = "D:/vscode/python/arquivos_temp/"     
 formato= ".mp4"

 yt = nome
 


 dest = "D:/biblioteca/"

 for a in os.listdir(fileDir):
      if a.endswith(".mp4"):
       os.rename(a,yt+formato)
 os.rename(dir_path+yt+formato,dest+yt+formato)       

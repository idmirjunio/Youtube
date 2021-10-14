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

def enviar_para_cruzamento(link,tipo):
 try:
  formato = ".mp4"    
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
    cruzador.unir_video_audio(nome=yt,formatovid= formato,formatoaud=formato)
 except:
  formato = ".webm"    
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
    cruzador.unir_video_audio(nome=yt,formatovid= formato,formatoaud=formato) 
        
#def saber_formato_video(nome):
    

#enviar_para_cruzamento(link=link,tipo="video")


def enviar_para_biblioteca(link): 
 
 formato= ".mp4"

 yt = YouTube(link).title
 


 dest = "D:/biblioteca/"

 for a in os.listdir(fileDir):
      if a.endswith(".mp4"):
       os.rename(a,yt+formato)
 os.rename(dir_path+yt+formato,dest+yt+formato)   


def enviar_para_local(nome):
 dir_path = "D:/vscode/python/arquivos_temp/"     
 formato= ".mp4"

 yt = nome
 


 dest = "D:/biblioteca/"

 for a in os.listdir(fileDir):
      if a.endswith(".mp4"):
       os.rename(a,yt+formato)
 os.rename(dir_path+yt+formato,dest+yt+formato)       

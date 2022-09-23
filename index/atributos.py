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
formatos= [".mp4",".webm",".3gpp",".opus"]
dest = "D:/vscode/python/arquivos_temp/"
def enviar_para_cruzamento(link,tipo):
 
  if tipo == "video":   
   yt = YouTube(link).title
   file ="(video)"
  
  else:
      if tipo == "audio": 
         yt = YouTube(link).title
         file = "(audio)"
 
  for a in os.listdir(fileDir):
     for i in formatos: 
        
       if a.endswith(i):
        os.rename(a,dest+file+i)

  #dir_path = os.path.dirname(os.path.realpath(__file__))


 

  
  if tipo == "audio":
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

def filtro_max(stream,tag,m_maior=0):
 res=0  
 
 for i in stream:
  res=0
  try:
   res=stream[i][tag]
   if res>m_maior:
      m_maior=res
  except: pass
  return m_maior
     
 
    
import moviepy.editor as mpe

def data_atual():
 from datetime import datetime

 # datetime object containing current date and time
 now = datetime.now()


 # dd/mm/YY H:M:S
 dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 return dt_string

    

def adicionar_biblioteca_json(nome):
 import json

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()

 data = data_atual() 

 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","w")

 y.update({nome:data})

 json.dump(y,x)

 x.close()
    

def unir_video_audio(nome,formatoaud,formatovid):
 import os
 import atributos   
 formato = ".mp4"
 aud=nome+"(audio)"+formatoaud
 vid=nome+"(video)"+formatovid
 out=nome+formato
 outname = "arquivos_temp/"+out
 audname = "arquivos_temp/"+aud
 vidname = "arquivos_temp/"+vid
 my_clip = mpe.VideoFileClip(vidname)
 audio_background = mpe.AudioFileClip(audname)
 final_clip = my_clip.set_audio(audio_background)
 final_clip.write_videofile(outname)
 adicionar_biblioteca_json(nome=nome)
 os.remove(audname)
 os.remove(vidname)
 atributos.enviar_para_local(nome=nome)



#unir_video_audio()


def  analisar_tudo():
 import json
 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()

 
 for x in y:
  unir_video_audio(nome=x)   
      
def analisar_algo(nome):
 import json
 x = open("D:/vscode/python/arquivos_temp/bibliotec.json","r")

 y = json.load(x)

 x.close()

 for x in y:
  if x == nome:
   return True
 return False 
       
    
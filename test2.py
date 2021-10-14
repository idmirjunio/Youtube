
from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


    

link = ("https://youtu.be/Gyroith0-Rc?list=RDGyroith0-Rc")
t = link.find("youtu.be")

if t != -1:
      print ("ok") 
#yt = YouTube(link, on_progress_callback = on_progress)


#x=yt.streams.filter(type="audio",adaptive=True)


#print(x)
#print(len(x))

#x= yt.streams.get_by_itag(251)

#x.download()
 

#tr = yt.streams.get_highest_resolution()

#titulo = yt.title
#imagem = yt.thumbnail_url
#print(imagem)

#import urllib.request
#import sys

#try:
 # urllib.request.urlretrieve(imagem, "pato.jpg")
#  print("Imagem salva! =)")
#except:
  #erro = sys.exc_info()
  #print("Ocorreu um erro:", erro)
#ys = yt.streams.get_highest_resolution()




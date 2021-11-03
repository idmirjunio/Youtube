
from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


    

link = ("https://www.youtube.com/watch?v=2R7Fyqeas4s")

yt = YouTube(link, on_progress_callback = on_progress)

x= yt.streams
x=yt.streams.filter(res="720p",adaptive=True)


print(x)
print(type(x))

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




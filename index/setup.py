import pytube
import atributos,ler_array


from pytube import YouTube, streams, Channel, Playlist
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()                 #copiar link do bloco de nota
link = win32clipboard.GetClipboardData()
#print(link)
win32clipboard.CloseClipboard()
link= "https://www.youtube.com/watch?v=QDLVSyBQHDU"
#YouTube(link).streams.get_highest_resolution()

#try:
 # yt=YouTube(link).streams.filter(adaptive=True).order_by("resolution").last()
yt=YouTube(link)


  #print(yt)
  #yt = YouTube(link).streams.fmt_streams
  #stream=atributos.transformar(url=yt)
  #print(stream)
#except:
try:
   yt = Playlist(link)
   for link in yt.video_urls:
    yt = YouTube(link).streams
    ler_array.inicio(yt=yt)     
    #yt = YouTube(url).streams.fmt_streams
    #stream=atributos.transformar(url=yt)
    #print(stream)
except:
   try:
    yt = Channel(link)
    for url in yt.video_urls:
     yt = YouTube(url).streams.fmt_streams
     stream=atributos.transformar(url=yt)
     #print(stream)
   except: 
    exit()

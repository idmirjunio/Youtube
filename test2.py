
from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard

win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()



yt=YouTube(link)

 


x= yt.streams.get_highest_resolution()

x.download()
 



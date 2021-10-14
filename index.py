import pytube


from pytube import YouTube, streams
from pytube.cli  import on_progress
link = ("https://youtu.be/Gyroith0-Rc?list=RDGyroith0-Rc")

yt = YouTube(link,on_progress_callback = on_progress)

print(yt.streams)
#steam = yt.streams.get_by_itag()
#steam.download()


from pytube import *
from pytube.cli  import main, on_progress
import pytube

link = "https://ww"

a="res"
b="1080p"
i=YouTube(link).check_availability()

print(i)
'''  
fps=None, res=None, resolution=None, mime_type=None, type=None, subtype=None, file_extension=None, abr=None, 
bitrate=None, video_codec=None, audio_codec=None, only_audio=None, only_video=None, progressive=None, adaptive=None, 
is_dash=None, custom_filter_functions=None
'''

preferencia_a={
    "stream1" : {
    "res" : "",
    "type":"",
    "subtype":"",
    "video_codec":"",
    "adaptive":"",
  }
}
preferencia_a={
    "stream1" : {
    "abr" : "",
    "type":"",
    "subtype":"",
    "audio_codec":"",
  }
}
preferencia_v_progress = {
  "stream1" : {
    "res" : "",
    "type":"video",
    "subtype":"mp4",
    "video_codec":"",
    "progressive":True,

  },
  "stream1" : {
    "res" : "",
    "type":"",
    "subtype":"",
    "video_codec":"",
    "progressive":"",
  },
  "stream1" : {
    "res" : "",
    "type":"",
    "subtype":"",
    "video_codec":"",
    "progressive":"",
  }
}
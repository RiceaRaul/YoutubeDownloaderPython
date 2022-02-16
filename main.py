import os
from yt_dlp import YoutubeDL
import json

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class YoutubeDownloading():
    def __init__(self):
        with open("music.txt","r") as f:
            self.MusicList = f.readlines()
            print("A fost generata lista de melodii")
            
    
    def startDownload(self):
        print(len(self.MusicList))
        for music in self.MusicList:
            self.downloadMusic(music)

    def downloadMusic(self,music):
        video_info = YoutubeDL({'format':'bestaudio/best','keepvideo':False,'logger': MyLogger(),}).extract_info(music,download=False)   
        if(video_info["webpage_url_basename"] == "watch"):
            filename = f"{video_info['title']}.mp3"
            filePath = os.path.join("Music",filename)
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filePath,
            }
            with YoutubeDL(options) as ydl:
                ydl.download([music])
        else:
            for musicPlaylist in video_info["entries"]:
                self.downloadMusic(musicPlaylist["original_url"])
        
if __name__=='__main__':
    yt = YoutubeDownloading()
    yt.startDownload()
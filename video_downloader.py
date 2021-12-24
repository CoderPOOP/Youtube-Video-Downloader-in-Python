# Youtube Video Downloader

from pytube import YouTube
url = input("Enter the Youtube video URL: ")
yt = YouTube(url)
video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
try:
    video.first().download()
    print("Download complete for: ", yt.title)
except Exception as e:
    print("Error! Download failed due to: ",e)
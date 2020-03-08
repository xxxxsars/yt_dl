from pytube import YouTube
from moviepy.editor import *
import os
import urllib.request
from bs4 import BeautifulSoup
import requests




def get_link(search_str :str):

    url = "https://www.youtube.com/results?search_query=" + search_str
    response =requests.get(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        print('https://www.youtube.com' + vid['href'])




url = 'https://www.youtube.com/watch?v=AKjgg3I6HEQ'
yt = YouTube(url)
video = yt.streams.first()
video.download()

dl_obj = yt.streams.first()
file_name = dl_obj.default_filename
without_extension_file_name = (os.path.splitext(dl_obj.default_filename)[0])
dl_obj.download()

video = VideoFileClip(file_name)
video.audio.write_audiofile(f"{without_extension_file_name}.mp3")

os.remove(file_name)
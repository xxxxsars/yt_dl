from pytube import YouTube
from moviepy.editor import *
import os
import urllib.request
from yt_crawler import yt_crawler

SAVE_PATH = "./convert"


# get first video and download it ,the response was the video name
def video_download(search : str) -> str:
    href = yt_crawler(search).get_href()[0]
    url = f'https://www.youtube.com{href}'
    yt = YouTube(url)
    video = yt.streams.first()
    video.download()
    dl_obj = yt.streams.first()
    file_name = dl_obj.default_filename
    dl_obj.download()

    return file_name



def conver_to_mp3(file_name :str):
    without_extension_file_name = (os.path.splitext(file_name)[0])
    video = VideoFileClip(file_name)

    if os.path.exists(SAVE_PATH) ==False:
        os.mkdir(SAVE_PATH)

    video.audio.write_audiofile(f"{SAVE_PATH}/{without_extension_file_name}.mp3")
    os.remove(file_name)
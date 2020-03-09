from bs4 import BeautifulSoup
import requests


class yt_crawler:
    def __init__(self,search_str:str):
        self.search_str = search_str

    def get_contents(self) ->list:
        url = "https://www.youtube.com/results?search_query=" + self.search_str
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        contents =  [ ]
        for all_mv in soup.select(".yt-lockup-video"):
            data = all_mv.select("a[rel='spf-prefetch']")
            if data!=None:
                contents.append(data)
        return contents

    def get_titles(self) -> list:
        titles = []
        for content in self.get_contents():
            titles.append(content[0].get("title"))
        return titles

    def get_href(self)->list:
        href = []
        for content in self.get_contents():
            href.append(content[0].get("href"))
        return href
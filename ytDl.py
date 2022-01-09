from __future__ import unicode_literals
import youtube_dl
import os
from youtube_search import YoutubeSearch
import json

# returns a dictionary
ydl_opts = {}
os.chdir('C:/Users/manue/Music/New')


def search_and_download(search_string, num_of_items, audio_bool=True):
    options = {}
    if audio_bool:
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False
        }

    results = YoutubeSearch(search_string, max_results=num_of_items).to_json()
    json2 = json.loads(results)
    i = 0
    for video in json2['videos']:
        with youtube_dl.YoutubeDL(options) as ydl:
            video_url = 'https://www.youtube.com' + video['url_suffix']
            print(video_url)
            ydl.download([video_url])
            i = i + 1


search = "metallica"
items = 20
audio = True
if __name__ == '__main__':
    search_and_download(search, items, audio)

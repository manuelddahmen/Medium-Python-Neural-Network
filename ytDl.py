from __future__ import unicode_literals
import youtube_dl
import os
from youtubesearch import youtubesearch_client
import json

# returns a dictionary
ydl_opts = {}
os.chdir('C:/Users/manue/Music/New')


def search_and_download(search_string, num_of_items, audio_bool=True):
    ydl_opts = {}
    if audio_bool:
        ydl_opts = {
            'format': 'bestaudio/best',
            # 'noplaylist': True,
            'continue_dl': True, -+

            "channel": "Angèlevl"
            # 'postprocessors': [{
            #     'key': 'FFmpegExtractAudio',
            #     'preferredcodec': 'mp3',
            #     'preferredquality': '192', }]
        }
    results = YoutubeSearch(search_string, max_results=num_of_items).to_json()
    json2 = json.loads(results)
    i = 0
    for video in json2['videos']:
        print(video)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                video_url = 'https://www.youtube.com' + video['url_suffix']
                print(video_url)
                ydl.download([video_url])
                i = i + 1
            except:
                print("An exception occurred")

    for url_suffix in url_suffixes:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                video_url = 'https://www.youtube.com' + url_suffix
                print(video_url)
                ydl.download([video_url])
                i = i + 1
            except:
                print("An exception occurred")


audio = False
search = ["Angèle"]
url_suffixes = []  # "?watch?v=ACMvpG5hDRw"
items = 80
if __name__ == '__main__':
    for s in search:
        search_and_download(s, items, audio)

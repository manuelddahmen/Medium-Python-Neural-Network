from __future__ import unicode_literals
import youtube_dl
import os
from youtube_search import YoutubeSearch
import json

results = YoutubeSearch('daft punk', max_results=20).to_json()

# returns a dictionary
ydl_opts = {}
os.chdir('C:/Users/manue/Music/New')

json = json.loads(results)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    i = 0
    for video in json['videos']:
        print(video)
        ydl.download(['https://www.youtube.com' + video['url_suffix']])
        i = i + 1

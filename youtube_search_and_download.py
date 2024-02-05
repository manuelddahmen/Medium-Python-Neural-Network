from pytube import Playlist
from pytube import Search
from pytube import Channel
import sys


# p = Channel(url="https://www.youtube.com/c/Ang%C3%A8levl")
# p = Playlist("https://music.youtube.com/playlist?list=OLAK5uy_lUUQjhyz1bZs83S4QGVDpCfFnCFLP5YA0")
# p = Playlist("https://www.youtube.com/watch?v=a79iLjV-HKw&list=OLAK5uy_ldqaJnerRG6N5EMGd9zytODtSRbcdjARU")
# p = Playlist("https://www.youtube.com/watch?v=UQCmuEO13Tc&list=PLD9pCIW090u1tql49d1ibxrUncLzaPvvf")
# p = Playlist("https://www.youtube.com/watch?v=8q_39S2YrMg&list=OLAK5uy_k8La2y_DRWHIAy6MStp0TTp5hswZDUeXY")

def download(arg):
    p = Search(arg)
    for video in p.results:  # p.videos
        print(video.title)
        try:
            st = video.streams.get_highest_resolution()
            st.download("C:\\Users\\manue\\Music\\New2")
        except:
            print("Error")
    print("done")


while True:
    print("Youtube search and download :")
    line = sys.stdin.readline()
    line = line.rstrip()
    print(line)
    download(line)
    print("Youtube search and download :")

# print("Done. End of script")

from pytube import Playlist
from pytube import Search
from pytube import Channel

# p = Channel(url="https://www.youtube.com/c/Ang%C3%A8levl")
p = Playlist("https://music.youtube.com/playlist?list=OLAK5uy_lUUQjhyz1bZs83S4QGVDpCfFnCFLP5YA0")
p = Playlist("https://www.youtube.com/watch?v=a79iLjV-HKw&list=OLAK5uy_ldqaJnerRG6N5EMGd9zytODtSRbcdjARU")
p = Playlist("https://www.youtube.com/watch?v=UQCmuEO13Tc&list=PLD9pCIW090u1tql49d1ibxrUncLzaPvvf")
p = Playlist("https://www.youtube.com/watch?v=8q_39S2YrMg&list=OLAK5uy_k8La2y_DRWHIAy6MStp0TTp5hswZDUeXY")
for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()

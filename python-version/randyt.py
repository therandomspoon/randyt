from __future__ import unicode_literals
import youtube_dl
print('please paste video url')
url=input()
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

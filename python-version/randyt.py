from __future__ import unicode_literals
import os
import time
import sys
import itertools
import threading
main = "185.27.134.55"
configmain = "185.27.134.140"
value = 'main'
value2 = 'dbconfigmain'
print('main =', value)
print('mainconfig =', value2)
print('accessing database')
print('mainframe')
print(' ERORR 502 invaid response')
print('redeploying')
print('success deployed as ARCH-Branch-26')
file = 0
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(3)
done = True
time.sleep(0.5)
os.system('clear')
import youtube_dl
print('please paste video url')
url=input()
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

import time
from tqdm import tqdm
link = input('>> ')
for i in tqdm(range(100)):
    time.sleep(0.015)
from pytube import YouTube
y = YouTube(link)
s = y.streams.get_highest_resolution()
print(s.default_filename)
s.download()

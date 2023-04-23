from pytube import YouTube
import os


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print('error')
    print('done')

link = input('>> ')
Download(link)

asd = input('do you want open the folder?(y/n) ')
if asd == 'y':
    os.startfile(r'D:/Video/Youtube')
else:
    pass